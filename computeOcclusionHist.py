import sys
import os
import math
import numpy as np
#from shelltools import run

gridfile = sys.argv[1]
gridfile2 = sys.argv[2]
outname = sys.argv[3]

infile = open(gridfile, 'r')
infile2 = open(gridfile2, 'r')
outfile = open(outname, 'w')

#nbvox = run('wc -l ' + infile)
#print(nbvox)

for i in range(0, 11):
    infile.readline()
    infile2.readline()
while True:
    line1 = infile.readline()
    line2 = infile2.readline()
    if not line1 or not line2 : break  # EOF
    
    #empty line
    if line1.strip():
        ns1 = [int(x) for x in line1.split()] 
        ns2 = [int(y) for y in line2.split()] 
        if len(ns1) != len(ns2) :
            print ("error the number of elements in two/three grids is not the same!!!")
            break
        for ind in range(0, len(ns1)):
            #print (ns1[ind], ns2[ind], ns1[ind] - ns2[ind], float(ns1[ind] - ns2[ind]) / ns1[ind])
            if ns1[ind] > 0 :
                val = 1 - float(ns1[ind] - ns2[ind]) / ns1[ind]

                if val > 1 :
                    val = 1
                outfile.write(str(100*val))
                outfile.write("\n")

#print(count)
infile.close()
infile2.close()
outfile.close()
