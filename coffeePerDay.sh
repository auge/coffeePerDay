#!/bin/bash

for i in `ls *.csv`
do
	c=`./analyze.py "$@" < $i`
	echo $i $c
done

