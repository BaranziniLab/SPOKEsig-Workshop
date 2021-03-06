# SPOKEsig-Workshop


Objectives of this workshop are as follows:


**1. To demonstrate how to fetch clinical EHR data using Patient Explorer**


**2. To demonstrate the usage of REST API to fetch SPOKEsig embedding vectors corresponding to the obtained EHR data** 


**3. To demonstrate the usage of SPOKEsig vectors in classifying patient population using a machine learning model**


&nbsp;


Follow the steps described below to follow the workshop


## Step 0: Check if python is installed into your local machine


Let us first make sure you have installed Python3 into your local machine. For that:


1. Open terminal (for Linux/MacOS) or Open Command Prompt (for Windows)


2. Copy-paste the following 
 
 
(Note: you can copy the following by clicking an icon that pops up at the right end of the line):



```
python --version
```


or


```
python3 --version
```


If you see **Python 3.x.x** you should be good to go. 


***Note: We have tested and verified that all codes in this repo will work on Python 3.6.x, Python 3.7.x and Python 3.8.x*** 


If Python3 is not installed in your machine, please install one of the above mentioned versions of Python3 before proceeding further.


&nbsp;


## Step 1: Clone this repo to your local machine


1. Open terminal (for Linux/MacOS) or Open Command Prompt (for Windows)


2. On the command line, copy and paste the following 



```
git clone https://github.com/BaranziniLab/SPOKEsig-Workshop.git 
```


3. Enter your GitHub credentials if asked.


4. Check if a folder named "SPOKEsig-Workshop" is created. If yes, Step 1 is completed


&nbsp;


## Step 2: Create a virtual environment, activate it and install python modules


First, check if virtualenv is installed in your local machine. For that, type the following:


```
virtualenv --version
```


If you see a version number on your screen, then you are good to go. Otherwise, type the following:


```
pip install virtualenv 
```


### For Linux/MacOS users


1. In the terminal, open "SPOKEsig-Workshop" folder that you just cloned. You can copy-paste the following:


```
cd SPOKEsig-Workshop
```


2. Once you are inside the folder, let us create a virtual environment. For that, copy-paste the following:


```
virtualenv -p $(which python3) venv
```


3. Activate the created virtual environment. For that, copy-paste the following:


```
source venv/bin/activate
```



4. To install the required python modules for this workshop, copy-paste the following:


```
pip install -r requirements.txt 
```


### For Windows users


1. In the cmd, open "SPOKEsig-Workshop" folder that you just cloned. You can copy-paste the following:


```
cd SPOKEsig-Workshop
```


2. Once you are inside the folder, let us create a virtual environment. 


For that, use the following syntax (**NB: DO NOT COPY PASTE**). 


```
virtualenv --python "\path\to\python.exe" venv
```


Change **"\path\to\python.exe"** to the path of python in your local machine. 


Usually path would be like (assuming you are using Python 3.6.x): 


**C:\Users\\<user_name>\AppData\Local\Programs\Python\Python36\python.exe**


3. Activate the created virtual environment. For that, copy-paste the following:


```
.\venv\Scripts\activate
```


4. To install the required python modules for this workshop, copy-paste the following:


```
pip install -r requirements.txt
```


&nbsp;


## Step 3: Spin up a Jupyter notebook instance in your local machine


In this workshop, we will run all codes in Jupyter notebook. Hence, type the following in your terminal(for Linux/MacOS)/CMD(for Windows) to start Jupyter notebook:


```
jupyter-notebook
```


This will spin up a jupyter notebook instance in your local machine. This notebook will appear in your browser


To use this instance, you will be prompted to enter a token. To get the token, check your terminal(for Linux/MacOS)/CMD(for Windows)


Once you furnish the token, you can see the contents of **SPOKEsig-Workshop** directory in your browser


**Note:** 


**If the notebook doesn't start automatically in your browser, copy and paste the link that appears on your terminal(for Linux/MacOS)/CMD(for Windows), The link will look like the following:**


***http\://localhost:8888/?token=***


Congratulations! you have successfully started Jupyter notebook in your local machine! 


Now, let us start running codes.


&nbsp;


## Step 4: Add API credentials to config file


For successfully running codes, we need to first add API credentials to **workshop.conf** file  


1. Open the file **workshop.conf** in **SPOKEsig-Workshop** directory


2. Change **&lt;API USERNAME&gt;** and **&lt;API PASSWORD&gt;** in the **[API]** section of the config file to username and password provided to you


3. Save the config file


&nbsp;


## Step 5: Create patient SPOKEsigs 


From this step onwards, you need to connect your UCSF VPN. 


In this step, we will create SPOKE signatures (a.k.a. SPOKEsigs) of patients using their clinical EHR data. For this, we make use of **PatientExplorer** to import clinical data of patients. 


***Please follow instructions in the presentation to know how to import clinical data from PatientExplorer***


Once the data is imported to your local machine, then:


1. You must have downloaded three csv files from PatientExplorer to your local machine such as a condition file, a medication file and a measurement file. As you might have noticed, these data correspond to three diseases such as breast_cancer, colon_cancer and irritable_bowel_syndrome. 


Rename these files as:


condition csv file --> ***breast_colon_ibd_conditions.csv***


medication csv file --> ***breast_colon_ibd_drugs.csv***


measurement csv file --> ***breast_colon_ibd_measurements_w_ab.csv***


2. Copy these renamed files to the folder **/data** in **SPOKEsig-Workshop** directory 


3. Open the folder **/code** in **SPOKEsig-Workshop** directory 


4. Open the notebook named **get_patient_spoke_sig_using_patient_explorer_and_API.ipynb**


5. As the name indicates, this notebook is used to create SPOKEsigs of patients that is imported from PatientExplorer. Notebook is well commented and hence, you can see that SPOKEsigs are obtained by making API calls whose credentials are saved at [Step 4](https://github.com/BaranziniLab/SPOKEsig-Workshop#step-4-add-api-credentials-to-config-file). 


6. Once you run all sections of this notebook, it saves three files to **/data** folder. Files are such as: a SPOKEsig numpy file (named **random_patient_spokesigs.npy**) and two flat files that provide information on patients (**random_patient_info.tsv** and **example_cohort.tsv**)  


Congratulations! You have now successfully created and saved SPOKEsigs of patients from PatientExplorer.


&nbsp;


## Step 6: Let us use the created SPOKEsigs on a machine learning model


Now we created SPOKEsigs of patients coming from three different disease categories such as breast_cancer, colon_cancer and irritable_bowel_syndrome.


Let us see if a machine learning model can make use of these SPOKEsigs and classify patients into these three different disease categories.


1. Open the notebook named **patient_spoke_sig_analysis.ipynb**


2. This notebook is also well commented. However, unlike previous notebook, this one has allocated some sections for you to fill. 


Don't worry! Useful links are provided at relevant sections for you to refer and fill out.  
If you still cannot figure out, you can always go to the [wiki](https://github.com/BaranziniLab/SPOKEsig-Workshop/wiki/Missing-code-snippets#find-the-missing-piece-of-code-from-here) section of this repo and see the missing portions of the code from there.


3. Once you run all sections of this notebook, you can see the performance of a machine learning model (random forest classifier) in classifying patient data into three disease categories using SPOKEsigs as its input.



&nbsp;

**Congratulations! You have successfully completed the hands-on session of this workshop.**

