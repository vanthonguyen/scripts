import sys
import os
import math
import numpy as np

def exportToFile(fileName, areaByZLevel, volumeByZLevel, minZ, resZ,volumeOfOneLevel):
#    print volumeOfOneLevel
    of = open(fileName,"w")
    for i in range(0,11):
        of.write("Dummy text for compatiblity with computree \n")

    for z in range(0, len(areaByZLevel)):
        coordZ = minZ + float(z)*resZ
        pad = areaByZLevel[z] / volumeOfOneLevel
        of.write("%d\t%d\t%f\t%f\t%f\t%f\n"% (z, z, areaByZLevel[z], volumeByZLevel[z], coordZ, pad))
    of.close()

gridfile =  sys.argv[1]

outPrefix = os.path.splitext(os.path.basename(gridfile))[0]

if len(sys.argv) > 2 :
    outPrefix = sys.argv[2] + "-"

infile = open(gridfile, 'r')

# Read parameters from header
bbox = [float(x) for x in infile.readline().split()] 
size = [float(x) for x in infile.readline().split()] 
dim = [int(x) for x in infile.readline().split()] 
numMaterial = int(infile.readline().split()[0]) #first number of this line

#profile
#areaByZ=np.empty(dim[2]); 
#areaByZ.fill(0)
#volumeByZ = np.empty(dim[2])
#volumeByZ.fill(0)
areaByZFull = np.zeros(dim[2])
volumeByZFull = np.zeros(dim[2])

#total = dim[0]*dim[1]*dim[3]
for x in range(0, dim[0]):
    for y in range(0, dim[1]):
        for z in range(0, dim[2]): 

            dat = [float(a) for a in infile.readline().split()] 
            
            if dat[0] != -1:
                #im = 0;
                for m in range(0, len(dat), 3):
                    #gridArea[x,yz,z,im] = dat[m + 1];
                    #gridVolume[x,yz,z,im] = dat[m + 2];
                    #im = im + 1;
                    #compute x,y coordinates
                    

                    #print x, y, (coordX - centerX) * (coordX - centerX) + (coordY - centerY) * (coordY - centerY ) 

                    areaByZFull[z] = areaByZFull[z] + dat[m + 1]
                    volumeByZFull[z] = volumeByZFull[z] + dat[m + 2]
                    #print coordX, coordY, centerX, centerY, radii
                    # check if y is in the cylindre
                        #print areaByZ[z], volumeByZ[z]

infile.close()

exportToFile(outPrefix + ".hist", areaByZFull, volumeByZFull, bbox[2], size[2], dim[0]*dim[1]*size[0]*size[1]*size[2])
