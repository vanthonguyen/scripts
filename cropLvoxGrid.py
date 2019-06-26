import sys
import os
import math
import numpy as np

gridfile = sys.argv[1]
nbx = int(sys.argv[2])
nby = int(sys.argv[3])
nbz = int(sys.argv[4])
outgrid = sys.argv[5]

infile = open(gridfile, 'r')
outfile = open(outgrid, 'w+')

outfile.write("ncols\t%d\n" % nbx)
outfile.write("nrows\t%d\n" % nby)
outfile.write("nzlev\t%d\n" % nbz)

oldNby = nby

for i in range(0, 11):
    line=infile.readline()
    if i > 2:
        outfile.write(line)
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
            if ix < nbx and iy > oldNby - nby - 1 and iz < nbz:
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
