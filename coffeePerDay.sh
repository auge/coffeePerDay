#!/bin/bash
for i in `ls *.csv`
do
	c=`sort -u $i | cut -d',' -f1,9 | grep -v NULL | ./analyze.py -c 1`
	echo $i $c
done

