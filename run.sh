
if [ $1 == "insert" ]
then
	python3 add.py

elif [ $1 == "display" ]
then
	python3 dis.py
elif [ $1 == "update" ]
then
	python3 Comp.py $2
elif [ $1 == "drop" ]
then
	python3 drop.py

elif [ $1 == "create" ]
then 
	python3 Tables.py


else
	cat help.txt
fi




