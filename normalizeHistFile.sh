#!/bin/bash

inFile=$1
coeff=$2
outFile=$3
awk -v coeff=$coeff '{if (NR < 12) {print $0} else print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6/coeff}' $inFile > $outFile 
