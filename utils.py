def readLvoxGridHeader(filename):
    infile = open(filename, 'r')
    headers = dict()
    for i in range(0,11):
        line = infile.readline()
        ns = [str(x) for x in line.split()] 
        k = ns[0]
        v = ns[1]
        if i < 3 or i == 9:
            v = int(ns[1])
        elif i < 9 : 
            v = float(ns[1])
        headers[k] = v
    infile.close()
    return headers

def readLvoxGridHeaderTuple(filename) :
    headers = readLvoxGridHeader(filename)
    return headers['ncols'], headers['nrows'], headers['nzlev'], headers['xllcorner'], headers['yllcorner'], headers['zllcorner'], headers['xcellsize'], headers['ycellsize'], headers['zcellsize'], headers['NODATA_value'], headers['datatype']


#def toHist(filename, grid, nx, ny, nz, normalizeHist) :
#    outhistfile = open(filename, 'w+')
#    for i in range(0,11):
#        outhistfile.write("Dummy text for compatiblity with computree \n")
#
#    coeff = 1
#    for z in range(0, nz): 
#        sumPadZ = 0
#        nbvoxOfPlot = 0
#        for y in range(0, ny):
#            for x in range(0, nx):
#                p = PADs[x,y,z]
#                if p > -7.999:
#                    nbvoxOfPlot += 1
#                if p < 0 and p > -1.1 and nbVoxs[z] > 0:
#                    p = padSumByZ[z]/nbVoxs[z]
#                    nbInter += 1
#                    sumInter += p
#                padStr = str(p)
#                if p.is_integer() :
#                    padStr = str(int(p))
#                outfile.write(padStr)
#                if x < nx - 1:
#                    outfile.write("\t")
#                if p > 0:
#                    sumPadZ += p
#            
#            outfile.write("\n")
#        print(z, nbInter, sumInter, nbVoxs[z], nbvoxOfPlot)
#        outfile.write("\n")
#        if normalizeHist:
#            coeff = nbvoxOfPlot
#        coordZ = zmin + z*zsize + zsize/2
#        outhistfile.write("%d\t%d\t%f\t%f\t%f\t%f\n"% (z, z, z, z, coordZ, sumPadZ/coeff))
#    
#    outfile.close()



#palettes = "#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"
#palettes = {"PAD": "#000000", "Point" : "C0", "Occlusion": "C5", "L-Architect": "C3"}
palettes = {"PAD": "#000000", "Point" : "C0", "Occlusion": "#E69F00", "L-Architect": "C3", "LAD": "C2"}
# PAD POINT 
