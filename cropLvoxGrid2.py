import sys
import os
import math
import numpy as np
from utils import readLvoxGridHeaderTuple

print("Crop for voxel origin from computree")

gridfile = sys.argv[1]
nbx = int(sys.argv[2])
nby = int(sys.argv[3])
nbz = int(sys.argv[4])
skipy = int(sys.argv[5])
outgrid = sys.argv[6]

infile = open(gridfile, 'r')
outfile = open(outgrid, 'w+')

nx, ny, nz, xmin, ymin, zmin, xsize, ysize, zsize, noda, dt = readLvoxGridHeaderTuple(gridfile)

outfile.write("ncols\t%d\n" % nbx)
outfile.write("nrows\t%d\n" % nby)
outfile.write("nzlev\t%d\n" % nbz)

oldNby = nby

for i in range(0, 11):
    line=infile.readline()
    if i > 2 and i != 4:
        outfile.write(line)
    if i == 4:
        oldyllcorner = float(line.split()[1])
        newyllcorner = oldyllcorner
        if skipy > 0:
            newyllcorner = oldyllcorner + skipy * ysize;
        outfile.write("yllcorner\t%f\n" % newyllcorner)
    elif i == 1:
        oldNby = int(line.split()[1])


ix = 0
iy = 0
iz = 0
count = 0
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
            #if ix < nbx and iy > skipy - 1 and iy < nby + skipy and iz < nbz:
            #if ix < nbx and iy > oldNby - nby - 1 and iz < nbz:
            if ix < nbx and iy > oldNby - nby - skipy - 1 and iy < oldNby - skipy and iz < nbz:
                outfile.write(str(pad))
                if ix < nbx - 1:
                    outfile.write("\t")
                elif ix == nbx - 1 :
                    outfile.write("\n")
            ix +=1
        iy += 1
    else:
        if iz < nbz:
            outfile.write(line) 
        iz += 1
        iy = 0

infile.close()
outfile.close()
