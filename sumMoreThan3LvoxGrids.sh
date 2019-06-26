#!/bin/zsh

nbGrid=$(($# -1))
echo $nbGrid

outFile=${@: -1}
firstFile=$1
for ((i = 2 ; i < nbGrid + 1 ; i++)); do
    rsFile=$(mktemp /tmp/sumlvox_XXXXXXXX)
    second=${!i}
    echo python sumLvoxGrid.py $firstFile $secondFile $rsFile 
    firstFile=$rsFile
done
mv $rsFile $outFile
rm -f /tmp/sumlvox_*
