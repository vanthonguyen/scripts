import sys
import os
import math
import numpy as np
from utils import readLvoxGridHeaderTuple

gridfile = sys.argv[1]
nifile = sys.argv[2]
nx, ny, nz, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(gridfile)
interpolatedfile = gridfile.replace('.GRD3DLVOX', '-interpolated.GRD3DLVOX')
histfile = gridfile.replace('.GRD3DLVOX', '-interpolated.hist')

infile = open(gridfile, 'r')
outfile = open(interpolatedfile, 'w+')
outhistfile = open(histfile, 'w+')
innifile = open(nifile, 'r')

for i in range(0, 11):
    line=infile.readline()
    outfile.write(line)
    innifile.readline() 

ix = 0
iy = 0
iz = 0
count = 0
padSumByZ = np.zeros(nz)
nbVoxNotZero = np.zeros(nz)
nbVoxAll = np.zeros(nz)
PADs = np.zeros((nx,ny,nz))
nis = np.zeros((nx,ny,nz))

while True:
    line = infile.readline()
    niline = innifile.readline()
    if not line : break  # EOF
    
    #empty line, finish a layer
    if line.strip():
        #sum value
        ix = 0
        ns = [float(x) for x in line.split()] 
        hits = [int(x) for x in niline.split()]  
        for ind in range(0, len(ns)):
            pad = ns[ind]
            #if ix < nbx and iy > oldNby - nby - 1 and iz < nbz:
            PADs[ix,iy,iz] = pad
            nis[ix,iy,iz] = hits[ind]
            if pad > 0:
               padSumByZ[iz] += pad
               nbVoxNotZero[iz] += 1
               #outfile.write(str(pad))
               # if ix < nbx - 1:
               #     outfile.write("\t")
               # elif ix == nbx - 1 :
               #     outfile.write("\n")
            if pad >= 0:
                nbVoxAll += 1
            ix +=1
        iy += 1
    else:
        iz += 1
        iy = 0


for i in range(0,11):
    outhistfile.write("Dummy text for compatiblity with computree \n")

for z in range(0, nz): 
    nbInter = 0
    sumInter = 0
    sumPadZ = 0
    for y in range(0, ny):
        for x in range(0, nx):
            p = PADs[x,y,z]
            if p < 0 and p > -1.1 :
                if nis[x,y,z] > 0:
                    if nbVoxNotZero[z] > 0:
                        p = padSumByZ[z]/nbVoxNotZero[z]
                elif nbVoxAll[z] > 0:
                    p = padSumByZ[z]/nbVoxAll[z]
                nbInter += 1
                sumInter += p
            padStr = str(p)
            if p.is_integer() :
                padStr = str(int(p))
            outfile.write(padStr)
            if x < nx - 1:
                outfile.write("\t")
            if p > 0 :
                sumPadZ += p
        
    outfile.write("\n")
    print(z, sumInter/(nbInter+1), nbInter, sumInter, nbVoxNotZero[z], nbVoxAll[z], "interpolate rate ", sumInter/(sumPadZ + 1))
    outfile.write("\n")
    coordZ = zmin + z*zsize + zsize/2
    outhistfile.write("%d\t%d\t%f\t%f\t%f\t%f\n"% (z, z, z, z, coordZ, sumPadZ))

outfile.close()


infile.close()
innifile.close()
outfile.close()
outhistfile.close()
