import sys
import os
import math
import numpy as np
#from shelltools import run
from utils import readLvoxGridHeaderTuple

gridfile = sys.argv[1]
centerX = float(sys.argv[2])
centerY = float(sys.argv[3])
outname = sys.argv[4]

nx, ny, nz, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(gridfile)

infile = open(gridfile, 'r')
outfile = open(outname, 'w')

MAX_R = 11.28
rstep = xsize
nr = int((MAX_R + 0.0001) / rstep)
hists = np.zeros((nr, nz))
counts = np.zeros((nr, nz))

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
        
            coordX = ix*xsize + xmin
            coordY = iy*ysize + ymin
            coordZ = iz*zsize + zmin
            dr = math.sqrt( (coordX - centerX)*(coordX - centerX) + (coordY - centerY)*(coordY - centerY)) 
            if dr <= MAX_R - rstep and val >= 0:
                ir = int(dr // rstep)
                hists[ir,iz] += val
                counts[ir,iz] += 1

            ix +=1
        iy += 1

    else:
        iz += 1
        iy = 0
       

for r in range(0, nr):
    for z in range(0, nz):
        #outfile.write(str(r * rstep) + "\t" + str(z * zsize) + "\t" + str(hists[r,z]/counts[r,z]) + "\n")
        oc = 1
        if counts[r,z] > 0 and hists[r,z] < counts[r,z] :
            oc = hists[r,z]/counts[r,z]
        outfile.write("%.1f %.1f %.2f %.1f %d\n" % (r * rstep, z * zsize, oc, hists[r,z], counts[r,z]))
#print(count)
infile.close()
outfile.close()
