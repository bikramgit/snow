#! /bin/bash

awk '{print $143,$144}' BUILD_NUMBER.txt > a.txt

awk '{print $2}' a.txt | cut -d'u' -f 2 > b.txt

cat b.txt | sed s/\'// > c.txt

cat c.txt | sed s/\'// > d.txt

cat d.txt | sed s/\,// > sys.txt

