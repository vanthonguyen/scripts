import sys
import math
import random

filename = sys.argv[1]
#percent of keeping points 0-100
keepingPercent = int(sys.argv[2])
outfile = sys.argv[3]

f = open(outfile,"w")

#print x, y, r
with open(filename) as pc: 
    for line in pc:
        if random.random() * 100 < keepingPercent :
            f.write(line)
f.close()
