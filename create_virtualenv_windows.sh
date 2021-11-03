echo Creating virtual environment ...
virtualenv venv

status=$?
if [ $status -eq 0 ]
then	
	echo virual environment is successfully created
else
	echo virtual environment is not created successfully
fi
