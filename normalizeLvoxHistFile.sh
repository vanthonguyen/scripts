#!/bin/bash

inFile=$1
gridFile=$2
outFile=$3
cols=`head -n1 $gridFile|awk '{print $2}'`
rows=`head -n2 $gridFile|tail -n1|awk '{print $2}'`
coeff=$((cols*rows))
awk -v coeff=$coeff '{if (NR < 12) {print $0} else print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6/coeff}' $inFile > $outFile 
