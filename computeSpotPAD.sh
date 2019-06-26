#!/bin/bash

nbVox=`wc -l < $1`
nbZ=$2
sumsurface=`awk '{ sum += $2; if ( NF == 6 ) { sum += $5 ; }} END{ print sum}' $1`
echo "number of voxel" $nbVox
echo "sum suface" $sumsurface 
