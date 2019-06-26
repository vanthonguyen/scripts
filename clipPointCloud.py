import sys
import math

filename = sys.argv[1]

xmin = -1
ymin = -1
#xmin = -11.28
#ymin = -11.28
zmin = sys.float_info.max
#xmax = 11.28
#ymax = 11.28
xmax = 1
ymax = 1 
zmax = sys.float_info.min

nbCoords = len(sys.argv) - 3
for ind in range(2, nbCoords + 2) :
    coord = float(sys.argv[ind])
    print (coord)
    #x
    if ind % 2 == 0:
        if coord < xmin :
            xmin = coord
        if coord > xmax :
            xmax = coord
    else :
        if coord < ymin:
            ymin = coord
        if coord > ymax:
            ymax = coord
outfile = sys.argv[len(sys.argv) - 1]

xmin -= 0.1
ymin -= 0.1
xmax += 0.1
ymax += 0.1

print(filename, xmin, xmax, ymin, ymax, zmin,zmax)
f = open(outfile,"w")

#skip first line
first=True
with open(filename) as pc: 
    for line in pc:
        if first : 
            first = False
            continue
        values = line.split()
        # check if this point is in the cylinder defined by x,y and r
        px = float(values[0])
        py = float(values[1])
        pz = float(values[2])
        if px > xmin and px < xmax and py > ymin and py < ymax :
            if pz < zmin :
                zmin = pz 
            if pz > zmax :
                zmax = pz 
            f.write(line)
print(filename, xmin, xmax, ymin, ymax, zmin,zmax)
f.close()
