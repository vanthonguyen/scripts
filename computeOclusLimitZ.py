import sys
import os
import math
import numpy as np
#from shelltools import run
from utils import readLvoxGridHeaderTuple

gridfile = sys.argv[1]

nx, ny, nz, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(gridfile)

infile = open(gridfile, 'r')

MAX_R = 11.28
MAX_Z = 25
SKIP_Z = 2.5
rstep = xsize
nr = int((MAX_R + 0.0001) / rstep)
nbVox = 0
nbNodata = 0

ix = 0
iy = 0
iz = 0

for i in range(0, 11):
    infile.readline()

while True:
    line = infile.readline()
    if not line : break  # EOF
    
    #empty line
    if line.strip():
        #sum value
        ix = 0
        ns = [float(x) for x in line.split()] 
        for ind in range(0, len(ns)):
            val = ns[ind]
            coordZ = iz*zsize + zmin
            #if dr <= MAX_R - 0.2 and val == -8 :
            #    print(dr, "something wrong")
            z = coordZ - zmin
            if z > SKIP_Z and val > -8:
                nbVox += 1
                if val == -1 :
                    nbNodata += 1

            ix +=1
        iy += 1

    else:
        iz += 1
        iy = 0
       
print ("nb NOdata /total nb of vox : nodata = %i/%i = %f" % (nbNodata, nbVox, nbNodata/nbVox))

infile.close()
