import sys
import os
import math
import numpy as np

def isInSpot1(x, centerX, y, centerY, radii):
    return math.sqrt((x - centerX)*(x - centerX) + (y - centerY)*(y - centerY)) <= radii

def isInSpot(x, centerX, y, centerY, radii, resX, resY):
    if isInSpot1(x - resX, centerX, y - resY, centerY, radii) :
        return True
    if isInSpot1(x - resX, centerX, y + resY, centerY, radii) :
        return True
    if isInSpot1(x + resX, centerX, y - resY, centerY, radii) :
        return True
    if isInSpot1(x + resX, centerX, y + resY, centerY, radii) :
        return True
    return False

def exportToFile(fileName, areaByZLevel, volumeByZLevel, minZ, resZ,volumeOfOneLevel):
    print volumeOfOneLevel
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
nbSpot = 4
radii = 3.0 
centerX = [7.5, 0   ,-7.5, 0   ]
centerY = [0.0, 7.5, 0,    -7.5]

# Read parameters from header
bbox = [float(x) for x in infile.readline().split()] 
size = [float(x) for x in infile.readline().split()] 
dim = [int(x) for x in infile.readline().split()] 
numMaterial = int(infile.readline().split()[0]) #first number of this line

# read grid
#gridArea = np.zeros((dim[0],dim[1], dim[2], numMaterial))
#gridVolume = np.zeros((dim[0],dim[1], dim[2], numMaterial))


#orig_stdout = sys.stdout
#outfile = open('profileSpot1', 'w')
#sys.stdout = outfile

#profile
#areaByZ=np.empty(dim[2]); 
#areaByZ.fill(0)
#volumeByZ = np.empty(dim[2])
#volumeByZ.fill(0)
areaByZ = np.zeros((nbSpot,dim[2]))
volumeByZ = np.zeros((nbSpot,dim[2]))

areaByZFull = np.zeros(dim[2])
volumeByZFull = np.zeros(dim[2])

#total = dim[0]*dim[1]*dim[3]
nbVoxSpot=np.zeros(nbSpot)

for x in range(0, dim[0]):
    for y in range(0, dim[1]):
        for z in range(0, dim[2]): 

            coordX = bbox[0] + float(x)*size[0]
            coordY = bbox[1] + float(y)*size[1]

            for spot in range(0, nbSpot):
                if isInSpot(coordX, centerX[spot], coordY, centerY[spot], radii, size[0], size[1]) :
                    nbVoxSpot[spot] += 1

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
                    for spot in range(0, nbSpot):
                        if isInSpot(coordX, centerX[spot], coordY, centerY[spot], radii, size[0], size[1]) :
                            areaByZ[spot][z] = areaByZ[spot][z] + dat[m + 1]
                            volumeByZ[spot][z] = volumeByZ[spot][z] + dat[m + 2]
                            print dat[m + 1]
                        #print areaByZ[z], volumeByZ[z]

infile.close()
print nbVoxSpot

for spot in range(0, nbSpot):
    exportToFile(outPrefix + "-spot" + str(spot + 1) + ".hist", areaByZ[spot], volumeByZ[spot], bbox[2], size[2], nbVoxSpot[spot]/dim[2]*size[0]*size[1]*size[2])
exportToFile(outPrefix + ".hist", areaByZFull, volumeByZFull, bbox[2], size[2], dim[0]*dim[1]*size[0]*size[1]*size[2])
