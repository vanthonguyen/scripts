import sys
import math

filename = sys.argv[1]
x = float(sys.argv[2])
y = float(sys.argv[3])
r = float(sys.argv[4])

outfile = sys.argv[5]
f = open(outfile,"w")

print x, y, r
with open(filename) as pc: 
    for line in pc:
        values = line.split()
        # check if this point is in the cylinder defined by x,y and r
        px = float(values[0])
        py = float(values[1])
        if math.sqrt( (x - px) * (x - px) + (y - py) * (y - py )) < r :
#            print  (x - px) * (x - px) + (y - py) * (y - py )
            f.write(line)
f.close()
