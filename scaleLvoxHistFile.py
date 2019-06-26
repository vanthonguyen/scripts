import sys
import os
import numpy as np


histFile = sys.argv[1]

downscaleFactor = int(sys.argv[2])

downscaleFile = sys.argv[3] 

outfile = open(downscaleFile, 'w')
#header
lineNumber = 0
nbHeader = 11
zIndex = 0
nbVar = 6

sumVals=np.zeros(nbVar)
nbRows=0
with open(histFile, 'r') as f:
    for line in f:
        if lineNumber < nbHeader :
            #header
            outfile.write(line)
        else:
            rowVals = [float(x) for x in line.split()]
            sumVals = sumVals + rowVals
            nbRows += 1
        lineNumber += 1
        if nbRows > 0 and nbRows % downscaleFactor == 0:
            outfile.write("%d\t%d\t%f\t%f\t%f\t%f\n"% (nbRows/downscaleFactor - 1, nbRows/downscaleFactor - 1, sumVals[2], sumVals[3], sumVals[4]/downscaleFactor, sumVals[5]/downscaleFactor))
            sumVals=np.zeros(nbVar)

if nbRows % downscaleFactor != 0:
    nbZ = nbRows % downscaleFactor
    outfile.write("%d\t%d\t%f\t%f\t%f\t%f\n"% (nbRows/downscaleFactor, nbRows/downscaleFactor, sumVals[2], sumVals[3], sumVals[4]/nbZ, sumVals[5]/nbZ))

outfile.close()
f.close()
