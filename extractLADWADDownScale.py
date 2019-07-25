import sys
import os
import math
import numpy as np

FACTOR=2
gridfile =  sys.argv[1]

fileNameLAD = "lad.GRD3DLVOX"
fileNameWAD = "wad.GRD3DLVOX"
ol = open(fileNameLAD,"w+")
ow = open(fileNameWAD, "w+")

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

ol.write("ncols\t%d\n" % ncols)
ol.write("nrows\t%d\n" % nrows)
ol.write("nzlev\t%d\n" % nzlev)

ol.write("xllcorner\t%f\n" % bbox[0])
ol.write("yllcorner\t%f\n" % bbox[1])
ol.write("zllcorner\t%f\n" % bbox[2])

ol.write("xcellsize\t%f\n" % (size[0]*FACTOR))
ol.write("ycellsize\t%f\n" % (size[1]*FACTOR))
ol.write("zcellsize\t%f\n" % (size[2]*FACTOR))

ol.write("NODATA_value\t-9\n")
ol.write("datatype\tfloat\n")
ol.flush()

ow.write("ncols\t%d\n" % ncols)
ow.write("nrows\t%d\n" % nrows)
ow.write("nzlev\t%d\n" % nzlev)

ow.write("xllcorner\t%f\n" % bbox[0])
ow.write("yllcorner\t%f\n" % bbox[1])
ow.write("zllcorner\t%f\n" % bbox[2])

ow.write("xcellsize\t%f\n" % (size[0]*FACTOR))
ow.write("ycellsize\t%f\n" % (size[1]*FACTOR))
ow.write("zcellsize\t%f\n" % (size[2]*FACTOR))

ow.write("NODATA_value\t-9\n")
ow.write("datatype\tfloat\n")

ow.flush()


#PADs = np.zeros((ncols,nrows,nzlev))
LADs = np.zeros((ncols,nrows,nzlev))
WADs = np.zeros((ncols,nrows,nzlev))
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
                    #leaf
                    if dat[m] == 0:
                        LADs[scaledX,scaledY,scaledZ] += dat[m + 1]/2/voxelVolume
                    else:
                        WADs[scaledX,scaledY,scaledZ] += dat[m + 1]/2/voxelVolume
                    #wood

infile.close()

for z in range(0, nzlev): 
    for y in range(0, nrows):
        for x in range(0, ncols):
            l = LADs[x,nrows - y - 1,z]

            ladStr = str(l)
            if l.is_integer() :
                ladStr = str(int(l))
            #oflat.write(padStr + "\n")
            ol.write(ladStr)
            if x < ncols - 1:
                ol.write("\t")
                    
            w = WADs[x,nrows - y - 1,z]
            wadStr = str(w)
            if w.is_integer() :
                wadStr = str(int(w))
            #oflat.write(padStr + "\n")
            ow.write(wadStr)
            if x < ncols - 1:
                ow.write("\t")
 
            #sumPadZ += p
        ol.write("\n")
        ow.write("\n")
    ol.write("\n")
    ow.write("\n")

#oflat.close()
ol.close()
ow.close()
