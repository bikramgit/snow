#! /bin/bash

#exec python /var/lib/jenkins/workspace/postmethod-job/poll-get-state.py
awk '{print $66,$67}' file1234 > e.txt

awk '{print $2}' e.txt | cut -d'u' -f 2 > f.txt

cat f.txt | sed s/\'// > g.txt

cat g.txt | sed s/\'// > h.txt

cat h.txt | sed s/\,// > i.txt

var=`awk 'NR==1 {print $0}' i.txt`

export var
echo $var
#echo "i'm here now"

if [ $var -lt 6 ]
then
	echo "before while"
	
	while [ $var -lt 6 ]
	do
		exec python /var/lib/jenkins/workspace/postmethod-job/poll-get-state.py
		awk '{print $66,$67}' file1234 > e.txt
		echo "i'm inside the loop"
		awk '{print $2}' e.txt | cut -d'u' -f 2 > f.txt

		cat f.txt | sed s/\'// > g.txt

		cat g.txt | sed s/\'// > h.txt

		cat h.txt | sed s/\,// > i.txt

		var=`awk 'NR==1 {print $0}' i.txt`


	done
else
	echo "job finished"
fi


#exec python /var/lib/jenkins/workspace/postmethod-job/poll-get-state.py "$var"

#echo $var

echo "hello i'm here"
