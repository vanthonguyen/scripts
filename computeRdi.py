import sys
import os
import math
import numpy as np

gridfile = sys.argv[1]
gridfile2 = sys.argv[2]
gridfile3 = sys.argv[3]

infile = open(gridfile, 'r')
infile2 = open(gridfile2, 'r')
infile3 = open(gridfile3, 'r')
outfile = open("rdi.GRD3DLVOX", 'w')
outpad = open("pad.GRD3DLVOX", 'w')

for i in range(0, 11):
    outfile.write(infile2.readline())
    outpad.write(infile3.readline())

for i in range(0, 3):
    infile.readline()

xCorner = float (infile.readline().split()[1])
yCorner = float (infile.readline().split()[1])
zCorner = float (infile.readline().split()[1])
xsize   = float (infile.readline().split()[1])
ysize   = float (infile.readline().split()[1])
zsize   = float (infile.readline().split()[1])

infile.readline()
infile.readline()

count = 0
ix = 0
iy = 0
iz = 0
while True:
    line1 = infile.readline()
    line2 = infile2.readline()
    line3 = infile3.readline()
    if not line1 or not line2 or not line3: break  # EOF
    
    #empty line
    if not line1.strip():
        outfile.write(line1) 
        outpad.write(line1) 
        iz = iz + 1
        iy = 0
    else:
        ix = 0
        ns1 = [int(x) for x in line1.split()] 
        ns2 = [int(x) for x in line2.split()] 
        ns3 = [int(x) for x in line3.split()] 
        if len(ns1) != len(ns2) or len(ns1) != len(ns3):
            print ("error the number of elements in two/three grids is not the same!!!")
            break
        for ind in range(0, len(ns1)):
            n = ns2[ind] - ns3[ind]
            rdi = -1
            pad = -1 
            if n > 0 :
                rdi = float(ns1[ind])/n
                if rdi >= 1 :
                    rdi = 0.99
                pad = -1.0*math.log10(1 - rdi)/xsize/0.5
 
            outfile.write(str(rdi))
            outpad.write(str(pad))
            if ind < len(ns1) - 1:
                outfile.write("\t")
                outpad.write("\t")
            else:
                outfile.write("\n")
                outpad.write("\n")
            ix = ix + 1
    iy = iy + 1

#print(count)
infile.close()
infile2.close()
infile3.close()
outfile.close()
outpad.close()
