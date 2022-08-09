#! /bin/bash

echo "<<- Installing Dependencies Please wait^__^ ->>"
sleep 2
apt install python
sleep 5
pip install smtplib
sleep 4
pip install subprocess
sleep 3
pip install time
sleep 2
pip install colorama
sleep 2
echo "<<- Dependencies Installed, You can launch tool ->>"
echo "Can I launch this Tool, y or Y for ok"
read var
if [[ $var == 'y' || $var == 'Y' ]] 
then
python3 PN.py

else
echo "Launch tool with this command python3 PN.py, Bye."
fi



