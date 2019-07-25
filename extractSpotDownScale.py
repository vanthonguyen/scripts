import sys
import os
import math
import numpy as np

FACTOR=2
gridfile =  sys.argv[1]

fileName = "ref.GRD3DLVOX"
fileNameFlat = "ref.flat"
of = open(fileName,"w+")
oflat = open(fileNameFlat, "w+")

if len(sys.argv) > 2 :
    FACTOR = int(sys.argv[2])

infile = open(gridfile, 'r')

# Read parameters from header
bbox = [float(x) for x in infile.readline().split()] 
size = [float(x) for x in infile.readline().split()] 
dim = [int(x) for x in infile.readline().split()] 
numMaterial = int(infile.readline().split()[0]) #first number of this line
#volumeByZ = np.zeros((nbSpot,dim[2]))

#total = dim[0]*dim[1]*dim[3]

ncols=int(math.ceil(float(dim[0]/FACTOR)))
nrows=int(math.ceil(float(dim[1]/FACTOR)))
nzlev=int(math.ceil(float(dim[2]/FACTOR)))

of.write("ncols\t%d\n" % ncols)
of.write("nrows\t%d\n" % nrows)
of.write("nzlev\t%d\n" % nzlev)

of.write("xllcorner\t%f\n" % bbox[0])
of.write("yllcorner\t%f\n" % bbox[1])
of.write("zllcorner\t%f\n" % bbox[2])

of.write("xcellsize\t%f\n" % (size[0]*FACTOR))
of.write("ycellsize\t%f\n" % (size[1]*FACTOR))
of.write("zcellsize\t%f\n" % (size[2]*FACTOR))

of.write("NODATA_value\t-9\n")
of.write("datatype\tfloat\n")

of.flush()
PADs = np.zeros((ncols,nrows,nzlev))
#LADs = np.zeros((ncols,nrows,nzlev))
#WADs = np.zeros((ncols,nrows,nzlev))
voxelVolume = size[0]*size[1]*size[2]*FACTOR*FACTOR*FACTOR

for x in range(0, dim[0]):
    for y in range(0, dim[1]):
        for z in range(0, dim[2]): 
            scaledX = x//FACTOR
            scaledY = y//FACTOR
            scaledZ = z//FACTOR
            dat = [float(a) for a in infile.readline().split()] 
            if dat[0] != -1:
                for m in range(0, len(dat), 3):
                    PADs[scaledX,scaledY,scaledZ] += dat[m + 1]/2/voxelVolume

infile.close()

for z in range(0, nzlev): 
    for y in range(0, nrows):
        for x in range(0, ncols):
            p = PADs[x,nrows - y - 1,z]
            padStr = str(p)
            if p.is_integer() :
                padStr = str(int(p))
            oflat.write(padStr + "\n")
            of.write(padStr)
            if x < ncols - 1:
                of.write("\t")
                    
            sumPadZ += p
        of.write("\n")
    of.write("\n")

oflat.close()
of.close()
