#!/bin/bash
for i in `ls *.csv`
do
	c=`sort -u $i | cut -d',' -f1,9 | grep -v NULL | ./analyze.py`
	echo $i $c
done

