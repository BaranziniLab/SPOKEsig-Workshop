# SPOKEsig-Workshop


Objectives of this workshop are as follows:


**1. To demonstrate how to fetch clinical EHR data using Patient Explorer**


**2. To demonstrate the usage of REST API to fetch SPOKEsig embedding vectors corresponding to the obtained EHR data** 


**3. To demonstrate the usage of SPOKEsig vectors in classifying patient population using a machine learning model**



Follow the steps described below to follow the workshop


## Step 0: Check if python is installed in your local machine


First, make sure you have installed python3 into your local machine. If you haven't, please download it from [here](https://www.python.org/downloads/). We recommend you to install python version of atleast 3.6 


## Step 1: Clone this repo to your local machine


1. Open terminal (for Linux/MacOS) or Open Command Prompt (for Windows)


2. On the command line, copy and paste the following 


(Note: you can copy the following by clicking an icon that pops at the right end of the line)


```
git clone https://github.com/BaranziniLab/SPOKEsig-Workshop.git 
```


3. Enter your GitHub credentials if asked.


4. Check if a folder named "SPOKEsig-Workshop" is created. If yes, Step 1 is completed


## Step 2: Create a virtual environment


### For Linux/MacOS users


1. In the terminal, open "SPOKEsig-Workshop" folder that you just cloned. You can copy-paste the following:


```
cd SPOKEsig-Workshop
```


2. Once you are inside the folder, let us create a virtual environment. For that, copy-paste the following:


```
virtualenv -p $(which python3) venv
```
