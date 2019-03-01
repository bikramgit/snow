#! /bin/bash

var=`awk 'NR==1 {print $0}' /var/lib/jenkins/workspace/postmethod-job/sys.txt`
#var1=2
export var
#export var1

echo " $var "
#sh var1.sh
exec python /var/lib/jenkins/workspace/postmethod-job/get.py "$var"
