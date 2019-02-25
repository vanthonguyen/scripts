#!/bin/bash

#10100317_v0.asc Z+F 0.0 0.0 1.5 0.036 0 180 0 360
#10100317_v1.asc Z+F 15.00000 0 1.5 0.036 0 180 0 360
#10100317_v2.asc Z+F 0 15.00000 1.5 0.036 0 180 0 360
#10100317_v3.asc Z+F -15.00000 0 1.5 0.036 0 180 0 360
#10100317_v4.asc Z+F 0 -15.00000 1.5 0.036 0 180 0 360
#scan 1

scan1=$1
scan2=$2
str1=`sed -n 2p $1`
str2=`sed -n 2p $2`

#echo $str1

x1=`echo $str1|awk '{print $2}'`
y1=`echo $str1|awk '{print $3}'`
z1=`echo $str1|awk '{print $4}'`

x2=`echo $str2|awk '{print $2}'`
y2=`echo $str2|awk '{print $3}'`
z2=`echo $str2|awk '{print $4}'`
x=`echo "($x1 + $x2)/2" |bc -l`
y=`echo "($y1 + $y2)/2" |bc -l`

printf "%0.4f %0.4f\n" $x $y
#x=$(bc -l <<< ($x1 + $x2)/2)
#echo $x
#printf "%f %f" "$(bc -l <<< ($x1 + $x2)/2)" "$(bc -l <<< ($y1 + $y2)/1)"
