#!/bin/sh 

h=$1
n=$2
o=${1/.hist/normalized.hist}
awk -v n=$n '{if (NR < 12) {print $0} else print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6/n}' $h > $o

