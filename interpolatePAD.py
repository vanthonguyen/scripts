import sys
import os
import math
import numpy as np

gridfile1 = sys.argv[1] #pad 10cm
gridfile2 = sys.argv[2] #pad 40cm
gridfile3 = sys.argv[3] #nb/nt 10cm
threshold = float(sys.argv[4])

interpolatefile = gridfile1.replace('.GRD3DLVOX', '-multi.GRD3DLVOX')

infile1 = open(gridfile1, 'r')
infile2 = open(gridfile2, 'r')
infile3 = open(gridfile3, 'r')
outfile = open(interpolatefile, 'w')


line = infile1.readline()
outfile.write(line)
nx1 = int (line.split()[1])

line = infile1.readline()
outfile.write(line)
ny1 = int (line.split()[1])

line = infile1.readline()
outfile.write(line)
nz1 = int (line.split()[1])

for i in range(0, 3):
    outfile.write(infile1.readline())

line = infile1.readline()
outfile.write(line)
xsize1 = float (line.split()[1])

for i in range(0,4):
    outfile.write(infile1.readline())

nx2 = int (infile2.readline().split()[1])
ny2 = int (infile2.readline().split()[1])
nz2 = int (infile2.readline().split()[1])

for i in range(0, 3):
    infile2.readline()
xsize2 = float (infile2.readline().split()[1])
for i in range(0,4):
    infile2.readline()

scaleFactor = int((xsize2 + 0.001)/xsize1)
print(xsize2, xsize1)
print ("factor",scaleFactor)

for i in range(0,11):
    infile3.readline()

#read grid2
grid2 = np.zeros((nx2 + 1, ny2 + 1, nz2 + 1))
ix2 = 0
iy2 = 0
iz2 = 0

while True:
    line2 = infile2.readline()
    if not line2 : break  # EOF
    
    #empty line
    if not line2.strip():
        iz2 += 1
        iy2 = 0
    else:
        ix2 = 0
        ns2 = [float(x) for x in line2.split()] 

        for ind in range(0, len(ns2)):

            grid2[ix2,iy2,iz2] = ns2[ind]
            #print (ix2,iy2,iz2,grid2[ix2,iy2,iz2])
            ix2 += 1

        iy2 += 1

#print(count)
infile2.close()


count = 0
sumInterpolated = 0
ix1 = 0
iy1 = 0
iz1 = 0

while True:
    line = infile1.readline()
    linenbnt = infile3.readline()
    if not line or not linenbnt : break  # EOF
    
    #empty line, finish a layer
    if line.strip():
        #sum value
        ix1 = 0
        ns = [float(x) for x in line.split()] 
        nbsurnts = [float(x) for x in linenbnt.split()] 

        if len(ns) != len(nbsurnts):
            print ("error the number of elements in two/three grids is not the same!!!")
            break
        for ind in range(0, len(ns)):
            interpolatedPad = ns[ind]
            occlusion = nbsurnts[ind]
            if occlusion > threshold  and interpolatedPad > -1.0001 :
                ix2 = int(ix1 / scaleFactor)
                iy2 = int(iy1 / scaleFactor)
                iz2 = int(iz1 / scaleFactor)
                interpolatedPad = grid2[ix2,iy2,iz2]
                #print(ix2, iy2, iz2, grid2[ix2,iy2,iz2],interpolatedPad)
                #print (ix1, iy1, iz1, ix2, iy2, iz2, grid2[ix2,iy2,iz2])
                #print ("new pad value", interpolatedPad)
                if interpolatedPad > 0 :
                    count += 1
                    sumInterpolated += interpolatedPad

            outfile.write(str(interpolatedPad))
            if ind < len(ns) - 1:
                outfile.write("\t")
            else:
                outfile.write("\n")
            ix1 +=1
        iy1 += 1

    else:
        outfile.write(line) 
        iz1 += 1
        iy1 = 0

print("interpolated :", count)
print("sum interpolated :", sumInterpolated)
infile1.close()
infile3.close()
outfile.close()
