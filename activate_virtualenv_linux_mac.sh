echo Activating virtual environment ...
source venv/bin/activate

status=$?
if [ $status -eq 0 ]
then	
	echo virual environment is activated
else
	echo virtual environment is not activated. Make sure virtual environment is created first.
fi