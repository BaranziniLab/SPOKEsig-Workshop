echo Did you create virtual envrionment? Press y or n

read varname

if [ $varname == "y" ]
then
	echo Did you activate virtual envrionment? Press y or n
	read varname2
	if [ $varname2 == "y" ] 
	then
		echo Installing modules now ...
		pip install -r requirements.txt	
		status=$?
		if [ $status -eq 0 ]
		then	
			echo Modules are installed successfully
		else
			echo Modules are not installed successfully
		fi
	elif [ $varname2 == "n" ]
	then
		echo Activate virtual envrionment first and then run this script
	else
		echo Your input is invalid. Try to press y or n as your input.
	fi
elif [ $varname == "n" ]
then
	echo Please create virtual envrionment first and then run this script
else
	echo Your input is invalid. Try to press y or n as your input.   
fi

