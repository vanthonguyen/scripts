import sys
import os
import math
import numpy as np
from utils import readLvoxGridHeaderTuple

#prefix = "beer"
#
#if len(sys.argv) > 1:
#    prefix = sys.argv[1]
#

v0pad = sys.argv[1]
v1pad = sys.argv[2]
v2pad = sys.argv[3]
v3pad = sys.argv[4]
v4pad = sys.argv[5]

v0nt = sys.argv[6]
v1nt = sys.argv[7]
v2nt = sys.argv[8]
v3nt = sys.argv[9]
v4nt = sys.argv[10]

v0nb = sys.argv[11]
v1nb = sys.argv[12]
v2nb = sys.argv[13]
v3nb = sys.argv[14]
v4nb = sys.argv[15]

N_THRESHOLD = 5

normalizeHist = False
isFirst = True
#read header of one
nx0, ny0, nz0, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(v0pad)
nx1, ny1, nz1, xmin1, ymin1, zmin1, xsize1, ysize1, zsize1, noda1, dt1 = readLvoxGridHeaderTuple(v1pad)
nx2, ny2, nz2, xmin2, ymin2, zmin2, xsize2, ysize2, zsize2, noda2, dt2 = readLvoxGridHeaderTuple(v2pad)
nx3, ny3, nz3, xmin3, ymin3, zmin3, xsize3, ysize3, zsize3, noda3, dt3 = readLvoxGridHeaderTuple(v3pad)
nx4, ny4, nz4, xmin4, ymin4, zmin4, xsize4, ysize4, zsize4, noda4, dt4 = readLvoxGridHeaderTuple(v4pad)

nx = min(nx0, nx1, nx2, nx3, nx4)
ny = min(ny0, ny1, ny2, ny3, ny4)
nz = min(nz0, nz1, nz2, nz3, nz4)

sumPADs = np.zeros((nx,ny,nz))
sumWeight = np.zeros((nx,ny,nz))

outfile = open( "merged-pad.GRD3DLVOX", 'w+')
outhistfile = open("merged.hist", 'w+')

outfile.write("ncols\t%d\n" % nx)
outfile.write("nrows\t%d\n" % ny)
outfile.write("nzlev\t%d\n" % nz)

outfile.write("xllcorner\t%f\n" % xmin)
outfile.write("yllcorner\t%f\n" % ymin)
outfile.write("zllcorner\t%f\n" % zmin)

outfile.write("xcellsize\t%f\n" % (xsize))
outfile.write("ycellsize\t%f\n" % (ysize))
outfile.write("zcellsize\t%f\n" % (zsize))

outfile.write("NODATA_value\t-9\n")
outfile.write("datatype\tfloat\n")




def isNotOcclu(pad, nt, nb) :
    return nt - nb > N_THRESHOLD and pad >= 0

def merge(padfile, ntfile, nbfile):
    inpad = open(padfile, 'r')
    innt = open(ntfile, 'r')
    innb = open(nbfile, 'r')

    global sumPADs
    global sumWeight
    
    for i in range(0, 11):
        inpad.readline()
        innt.readline()
        innb.readline()

    ix = 0
    iy = 0
    iz = 0
    while True:
        linepad = inpad.readline()
        linent = innt.readline()
        linenb = innb.readline()

        if not linepad or not linent or not linenb: break  # EOF

        if linepad.strip():
            #sum value
            ix = 0
            pads = [float(x) for x in linepad.split()] 
            nts = [int(x) for x in linent.split()] 
            nbs = [int(x) for x in linenb.split()] 

            for ind in range(0, len(pads)):
                if ix >= nx or iy >= ny or iz >= nz :
                    continue
                pad = pads[ind]
                nt = nts[ind]
                nb = nbs[ind]

                if isNotOcclu(pad, nt, nb) :
                    w = nt - nb
                    sumPADs[ix,iy,iz] += w*pad
                    sumWeight[ix,iy,iz] += w
                ix +=1
            iy += 1
        else:
            #if iz < nbz:
            #    outfile.write(line) 
            iz += 1
            iy = 0

    print(sumPADs)
    inpad.close()
    innt.close()
    innb.close()


for i in range(0,11):
    outhistfile.write("Dummy text for compatiblity with computree \n")

#merge process

merge(v0pad,v0nt,v0nb)
merge(v1pad,v1nt,v1nb)
merge(v2pad,v2nt,v2nb)
merge(v3pad,v3nt,v3nb)
merge(v4pad,v4nt,v4nb)


coeff = 1
for z in range(0, nz): 
    sumPadZ = 0
    nbvoxOfPlot = 0
    for y in range(0, ny):
        for x in range(0, nx):
            if sumWeight[x,y,z] > 0 :
                sumPADs[x,y,z] /= sumWeight[x,y,z]
            p = sumPADs[x,y,z] 

            if p > -7.999:
                nbvoxOfPlot += 1

            padStr = str(p)
            if p.is_integer() :
                padStr = str(int(p))

            if p > 0:
                sumPadZ += p
        
            outfile.write(padStr)
            if x < nx - 1:
                outfile.write("\t")
        outfile.write("\n")
    outfile.write("\n")
    if normalizeHist:
        coeff = nbvoxOfPlot
    coordZ = zmin + z*zsize + zsize/2
    outhistfile.write("%d\t%d\t%f\t%f\t%f\t%f\n"% (z, z, z, z, coordZ, sumPadZ/coeff))

outfile.close()
outhistfile.close()
