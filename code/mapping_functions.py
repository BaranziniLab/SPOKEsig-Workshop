import pandas as pd
import numpy as np
import os
import requests
from requests.auth import HTTPBasicAuth
from retrying import retry
import warnings
from config import read_config

def get_patient_info(all_rdb_db, cohort_patient_info_file):
    patient_info_df = pd.read_csv(cohort_patient_info_file, sep='\t', header=0, index_col=False)
    # use only patients with demographic data
    all_rdb_db = pd.merge(all_rdb_db, patient_info_df[['patient_id']], on='patient_id')
    # get number of SEPs per patient
    sep_count = all_rdb_db[['patient_id', 'SPOKE_ID']].drop_duplicates().groupby('patient_id').count().reset_index().rename(index=str, columns={'SPOKE_ID':'SEP_Count'})
    patient_info_df = pd.merge(patient_info_df, sep_count, on='patient_id')
    # get number of OMOP per patient
    ehr_count = all_rdb_db[['patient_id', 'concept_id']].drop_duplicates().groupby('patient_id').count().reset_index().rename(index=str, columns={'concept_id':'OMOP_Count'})
    patient_info_df = pd.merge(patient_info_df, ehr_count, on='patient_id')
    del sep_count, ehr_count
    return patient_info_df, all_rdb_db

def load_and_filter_rdb_data(diag_filename, med_filename, lab_filename, cohort_patient_info_file, omop_to_spoke):
    file_list = [diag_filename, med_filename, lab_filename]
    col_change = [{"icd10_code":'ICD10CM',"icd9_code":'ICD9CM'}, {'medication_id':'MED'}, {'lab_component_id':'LAB'}]
    domain_list = ['Condition', 'Drug', 'Measurement']
    all_rdb_db = pd.DataFrame(columns=['patient_id','rdb_id'])
    for i, (filename, col_change_dict) in enumerate(zip(file_list, col_change)):
        df = pd.read_csv(filename, header=0, index_col=False).rename(columns=col_change_dict)
        if domain_list[i] == 'Measurement':
            df = df[df.lab_result_abnormal=='Yes'].drop(['lab_result_abnormal'],axis=1)
        for col in list(col_change_dict.values()):
            df.loc[:,col] = ['%s:%s' % (col, rdb) for rdb in df[col].values]
            all_rdb_db = pd.concat((all_rdb_db, df[['patient_id', col]].rename(index=str, columns={col:'rdb_id'})),axis=0)
        del df
    print(all_rdb_db.patient_id.unique().shape)
    all_rdb_db = pd.merge(all_rdb_db.rename(columns={'rdb_id':'Node_ID'}), omop_to_spoke[['Node_ID', 'concept_id', 'SPOKE_ID']], on='Node_ID')
    all_rdb_db.loc[:, 'concept_id'] = ['OMOP:%s' % concept_id for concept_id in all_rdb_db.concept_id.values]
    # get patient information
    patient_info_df, all_rdb_db = get_patient_info(all_rdb_db, cohort_patient_info_file)
    all_rdb_db = all_rdb_db.drop(['Node_ID'], axis=1).drop_duplicates()
    print(all_rdb_db.patient_id.unique().shape)
    return all_rdb_db, patient_info_df

def add_diseases_to_patient_info(disease_list, all_rdb_db, patient_info_df, node_info_df):
    disease_names = ['_'.join(node_info_df[node_info_df.Node==disease].Node_Name.values[0].split()) for disease in disease_list]
    # make df with patients and target diseases
    disease_df = all_rdb_db[['patient_id', 'SPOKE_ID']][all_rdb_db.SPOKE_ID.isin(disease_list)].drop_duplicates().drop_duplicates(subset=['patient_id'], keep=False)
    # add to patient info
    patient_info_df = pd.merge(patient_info_df, disease_df, on='patient_id').sort_values('Patient_Index')
    # add label
    patient_info_df.loc[:,'label'] = patient_info_df.SPOKE_ID.map(dict(zip(disease_list, np.arange(len(disease_list)))))
    # add disease names
    patient_info_df.loc[:,'Disease'] = patient_info_df.SPOKE_ID.map(dict(zip(disease_list, disease_names)))
    return patient_info_df

def load_or_make_spokesig_mean_std_dist(node_info_df, example_cohort, diseases, disease_names, data_path, load_data=True):
    mean_sig_file = os.path.join(data_path, 'mean_sig.npy')
    std_sig_file = os.path.join(data_path, 'std_sig.npy')
    patient_to_disease_dist_file = os.path.join(data_path, 'patient_to_disease_dist.npy')
    if load_data == False:
        # load spoke sigs
        spoke_sigs = np.load(int_spoke_sig_filename, allow_pickle=False)
        mean_sig = np.mean(spoke_sigs, axis=0)
        # get mean of SPOKEsigs
        np.save(mean_sig_file, mean_sig, allow_pickle=False)
        # get std of SPOKEsigs
        std_sig = np.std(spoke_sigs, axis=0)
        np.save(std_sig_file, std_sig, allow_pickle=False)
        # convert to z score (saving mean and std)
        spoke_sigs = np.nan_to_num((spoke_sigs-mean_sig)/std_sig)
        # create distance matrix
        patient_to_disease_dist = cdist(spoke_sigs, psev_matrix, metric='cosine')
        np.save(patient_to_disease_dist_file, patient_to_disease_dist, allow_pickle=False)
        # mean node value per disease
        mean_node_val_df = node_info_df.drop_duplicates()
        for disease, name in zip(diseases, disease_names):
            mean_node_val_df.loc[:,name] = np.mean(spoke_sigs[example_cohort[example_cohort.Disease==disease].Patient_Index.values], axis=0)
        del spoke_sigs
        mean_node_val_df.to_csv('mean_node_val_df.tsv', sep='\t', header=True, index=False)
    else:
        mean_sig = np.load(mean_sig_file, allow_pickle=False)
        std_sig = np.load(std_sig_file, allow_pickle=False)
        patient_to_disease_dist = np.load(patient_to_disease_dist_file, allow_pickle=False)
    return mean_sig, std_sig, patient_to_disease_dist
