# get filename and dirname in folder
#input: absolute path of inquiring folder

#Recursive fuction
function Fun()
{
	if [ -d "$1" ]
	then
		echo $1 >>dirnames.txt
		dirnames=$(ls -A $1) #-A parameter enables to list dirs and files starting with ._ but except . and ..
		for dirname in $dirnames
		do
			dirname=${1}"/"${dirname}
			Fun $dirname
		done
	elif [ -f "$1" ]
	then
		echo $1 >>filenames.txt
	fi
}


real_path=$(realpath $1)
if [ -n "$1" ]
then
	echo "The inquiring folder is $real_path"
	Fun $real_path
else
	echo "Please input the real path of inquiring folder"
fi
