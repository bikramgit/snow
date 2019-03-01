#! /bin/bash

var=`awk 'NR==2{print $0}' sys.txt`

echo "$var"

export var
#var1=7836378273787389634767878923476247878924762478682478683468
#export var1

#var2=$var
#export var2
#echo "$var2"


#echo " $var "
#sh var1.sh
exec python /var/lib/jenkins/workspace/postmethod-job/time.py "$var"

