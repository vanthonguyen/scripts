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


#palettes = "#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"
#palettes = {"PAD": "#000000", "Point" : "C0", "Occlusion": "C5", "L-Architect": "C3"}
palettes = {"PAD": "#000000", "Point" : "C0", "Occlusion": "#E69F00", "L-Architect": "C3"}
# PAD POINT 
