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


**For Linux/MacOS users**


If you see something like **Python 3.x.x** on your screen, then you are good to go. Otherwise, please download Python3 from [here](https://www.python.org/downloads/release/python-368/). 


**For Windows users**


If you see something like **Python 3.6.x** on your screen, then you are good to go. Otherwise, please download Python3.6 from [here](https://www.python.org/downloads/release/python-368/). When you open this link, use "Windows x86-64 executable installer" to install Python 3.6.8 into your local machine.



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


For that, use the following syntax (NB: DO NOT COPY PASTE). Change "\path\to\python.exe" to the path of python in your local machine. 


Usually path would be like (assuming you are using Python 3.6.x): 


**C:\Users\\<user_name>\AppData\Local\Programs\Python\Python36\python.exe**


```
virtualenv --python "\path\to\python.exe" venv
``` 


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


Congratulations, you have successfully started Jupyter notebook in your local machine! 


Now, let us start running codes.


&nbsp;


## Step 4: Add API credentials to config file


For successfully running codes, we need to first add API credentials to **workshop.conf** file  


1. Open the file **workshop.conf** in **SPOKEsig-Workshop** directory


2. Change **&lt;API USERNAME&gt;** and **&lt;API PASSWORD&gt;** in the **[API]** section of the config file to username and password provided to you


3. Save the config file


&nbsp;


## Step 5: Create patient SPOKEsigs 


In this step, we will create SPOKE signatures (a.k.a. SPOKEsigs) of patients using their clinical EHR data. For this, we make use of **PatientExplorer** to import clinical data of patients. 


***Please follow instructions in the presentation to know how to import clinical data from PatientExplorer***


Once the data is imported to your local machine, then:


a. You must have downloaded three csv files to your local machine such as a condition file, a medication file and a measurement file. 


Rename these files as:


condition csv file --> ***breast_colon_ibd_conditions.csv***


medication csv file --> ***breast_colon_ibd_drugs.csv***


measurement csv file --> ***breast_colon_ibd_measurements_w_ab.csv***


b. Copy these renamed files to the folder **/data** in **SPOKEsig-Workshop** directory 


c. Open the folder **/code** in **SPOKEsig-Workshop** directory 


d. Open the notebook named **get_patient_spoke_sig_using_patient_explorer_and_API.ipynb**
