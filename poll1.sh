#! /bin/bash


awk '{print $66,$67}' get-data.txt > e.txt

awk '{print $2}' e.txt | cut -d'u' -f 2 > f.txt

cat f.txt | sed s/\'// > g.txt

cat g.txt | sed s/\'// > h.txt

cat h.txt | sed s/\,// > i.txt

var=`awk 'NR==2 {print $0}' i.txt`

export var

exec python /var/lib/jenkins/workspace/postmethod-job/get-state.py "$var"
