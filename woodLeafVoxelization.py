import sys
import os
import math
import numpy as np
from utils import readLvoxGridHeaderTuple

#grid file for parameter

gridfile = sys.argv[1]
cloudFile = sys.argv[2]
#lf = "leaves.GRD3DLVOX"
#wf = "woods.GRD3DLVOX"
wf = sys.argv[3]
lf = sys.argv[4]

nx, ny, nz, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(gridfile)

ow = open( wf, 'w+')
ol = open( lf, 'w+')

ol.write("ncols\t%d\n" % nx)
ol.write("nrows\t%d\n" % ny)
ol.write("nzlev\t%d\n" % nz)
ol.write("xllcorner\t%f\n" % xmin)
ol.write("yllcorner\t%f\n" % ymin)
ol.write("zllcorner\t%f\n" % zmin)
ol.write("xcellsize\t%f\n" % (xsize))
ol.write("ycellsize\t%f\n" % (ysize))
ol.write("zcellsize\t%f\n" % (zsize))
ol.write("NODATA_value\t-9\n")
ol.write("datatype\tfloat\n")

ow.write("ncols\t%d\n" % nx)
ow.write("nrows\t%d\n" % ny)
ow.write("nzlev\t%d\n" % nz)
ow.write("xllcorner\t%f\n" % xmin)
ow.write("yllcorner\t%f\n" % ymin)
ow.write("zllcorner\t%f\n" % zmin)
ow.write("xcellsize\t%f\n" % (xsize))
ow.write("ycellsize\t%f\n" % (ysize))
ow.write("zcellsize\t%f\n" % (zsize))
ow.write("NODATA_value\t-9\n")
ow.write("datatype\tfloat\n")


wps = np.zeros((nx,ny,nz))
lps = np.zeros((nx,ny,nz))

with open(cloudFile) as pc: 
    for line in pc:
        values = line.split()
        # check if this point is in the cylinder defined by x,y and r
        px = float(values[0])
        py = float(values[1])
        pz = float(values[2])
        xindex = int((px - xmin)//xsize)
        yindex = int((py - ymin)//ysize)
        zindex = int((pz - zmin)//zsize)
        red = float(values[3])
        #wood
        if red > 0.000000001:
            wps[xindex, yindex, zindex] += 1
        else:
            lps[xindex, yindex, zindex] += 1

print(lps.sum(), wps.sum())
for z in range(0, nz): 
    for y in range(0, ny):
        for x in range(0, nx):
            l = lps[x,ny - y - 1,z]

            lStr = str(l)
            if l.is_integer() :
                lStr = str(int(l))
            #oflat.write(padStr + "\n")
            ol.write(lStr)
            if x < nx - 1:
                ol.write("\t")
                    
            w = wps[x,ny - y - 1,z]
            wStr = str(w)

            if w.is_integer() :
                wStr = str(int(w))

            ow.write(wStr)
            if x < nx - 1:
                ow.write("\t")
 
            #sumPadZ += p
        ol.write("\n")
        ow.write("\n")
    ol.write("\n")
    ow.write("\n")

#oflat.close()
ol.close()
ow.close()
