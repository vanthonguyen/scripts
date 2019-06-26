import sys
import os
import math
import numpy as np
from utils import readLvoxGridHeaderTuple

FACTOR=2
gridfile =  sys.argv[1]
nfile =  sys.argv[2]

fileName = "downscaledWeighted.GRD3DLVOX"
of = open(fileName,"w+")
#oflat = open(fileNameFlat, "w+")

if len(sys.argv) > 3 :
    FACTOR = int(sys.argv[3])

infile = open(gridfile, 'r')
innfile = open(nfile, 'r')

nx, ny, nz, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(gridfile)

ncols=int(math.ceil(float(nx/FACTOR)))
nrows=int(math.ceil(float(ny/FACTOR)))
nzlev=int(math.ceil(float(nz/FACTOR)))

of.write("ncols\t%d\n" % ncols)
of.write("nrows\t%d\n" % nrows)
of.write("nzlev\t%d\n" % nzlev)

of.write("xllcorner\t%f\n" % xmin)
of.write("yllcorner\t%f\n" % ymin)
of.write("zllcorner\t%f\n" % zmin)

of.write("xcellsize\t%f\n" % (xsize*FACTOR))
of.write("ycellsize\t%f\n" % (ysize*FACTOR))
of.write("zcellsize\t%f\n" % (zsize*FACTOR))

of.write("NODATA_value\t-9\n")
of.write("datatype\tfloat\n")

of.flush()
###incomplete
PADs = np.zeros((ncols,nrows,nzlev))
nbSum = np.zeros((ncols,nrows,nzlev))
isOutside = np.zeros((ncols,nrows,nzlev), dtype=bool)
#originalPADs = np.zeros((nx,ny,nz))
#voxelVolume = size[0]*size[1]*size[2]*FACTOR*FACTOR*FACTOR

#skip headers
for i in range(0, 11):
    line = infile.readline()
    innfile.readline()

ix = 0
iy = 0
iz = 0
count = 0
#read original PADs
while True:
    line = infile.readline()
    nline = innfile.readline()
    if not line or not nline : break  # EOF
    
    #empty line, finish a layer
    if line.strip():
        #sum value
        ix = 0
        ns = [float(x) for x in line.split()] 
        shots = [int(x) for x in nline.split()] 
        for ind in range(0, len(ns)):

            scaledX = ix//FACTOR
            scaledY = iy//FACTOR
            scaledZ = iz//FACTOR
            pad = ns[ind]
            coef = shots[ind]
            if pad >= 0:
                PADs[scaledX,scaledY,scaledZ] += pad*coef
                nbSum[scaledX,scaledY,scaledZ] += coef
            elif pad == -8:
                isOutside[scaledX,scaledY,scaledZ] = True
            ix +=1
        iy += 1
    else:
        iz += 1
        iy = 0

infile.close()
innfile.close()

for z in range(0, nzlev): 
    for y in range(0, nrows):
        for x in range(0, ncols):
            p = PADs[x,y,z]
            nbs = nbSum[x,y,z]
            outside = isOutside[x,y,z]
            newPad = -8 # doesnot exist in virtual plots
            if nbs > 0 :
                newPad = p /nbs
            elif not outside :
                newPad = -1
            padStr = str(newPad)
            if p.is_integer() :
                padStr = str(int(newPad))
            #oflat.write(padStr + "\n")
            of.write(padStr)
            if x < ncols - 1:
                of.write("\t")
        of.write("\n")
    of.write("\n")

#oflat.close()
of.close()
