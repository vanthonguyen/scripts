import sys
import os
import math
import numpy as np
from utils import readLvoxGridHeaderTuple

gridfile = sys.argv[1]
nx, ny, nz, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(gridfile)
interpolatedfile = gridfile.replace('.GRD3DLVOX', '-interpolated.GRD3DLVOX')
histfile = gridfile.replace('.GRD3DLVOX', '-interpolated.hist')

infile = open(gridfile, 'r')
outfile = open(interpolatedfile, 'w+')
outhistfile = open(histfile, 'w+')

for i in range(0, 11):
    line=infile.readline()
    outfile.write(line)
normalizeHist = False
if len(sys.argv) > 2 :
    normalizeHist = True

ix = 0
iy = 0
iz = 0
count = 0
padSumByZ = np.zeros(nz)
nbVoxs = np.zeros(nz)
PADs = np.zeros((nx,ny,nz))

while True:
    line = infile.readline()
    if not line : break  # EOF
    
    #empty line, finish a layer
    if line.strip():
        #sum value
        ix = 0
        ns = [float(x) for x in line.split()] 
        for ind in range(0, len(ns)):
            pad = ns[ind]
            #if ix < nbx and iy > oldNby - nby - 1 and iz < nbz:
            PADs[ix,iy,iz] = pad
            if pad >= 0:
               padSumByZ[iz] += pad
               nbVoxs[iz] += 1
               #outfile.write(str(pad))
               # if ix < nbx - 1:
               #     outfile.write("\t")
               # elif ix == nbx - 1 :
               #     outfile.write("\n")
            ix +=1
        iy += 1
    else:
        iz += 1
        iy = 0


for i in range(0,11):
    outhistfile.write("Dummy text for compatiblity with computree \n")

coeff = 1
for z in range(0, nz): 
    nbInter = 0
    sumInter = 0
    sumPadZ = 0
    nbvoxOfPlot = 0
    for y in range(0, ny):
        for x in range(0, nx):
            p = PADs[x,y,z]
            if p > -7.999:
                nbvoxOfPlot += 1
            if p < 0 and p > -1.1 and nbVoxs[z] > 0:
                p = padSumByZ[z]/nbVoxs[z]
                nbInter += 1
                sumInter += p
            padStr = str(p)
            if p.is_integer() :
                padStr = str(int(p))
            outfile.write(padStr)
            if x < nx - 1:
                outfile.write("\t")
            if p > 0:
                sumPadZ += p
        
        outfile.write("\n")
    print(z, nbInter, sumInter, nbVoxs[z], nbvoxOfPlot)
    outfile.write("\n")
    if normalizeHist:
        coeff = nbvoxOfPlot
    coordZ = zmin + z*zsize + zsize/2
    outhistfile.write("%d\t%d\t%f\t%f\t%f\t%f\n"% (z, z, z, z, coordZ, sumPadZ/coeff))

outfile.close()


infile.close()
outfile.close()
outhistfile.close()
