import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
#from scipy.interpolate import griddata

from scipy.interpolate import interp2d
 
matplotlib.rcParams.update({'font.size': 8})
#matplotlib.rcParams.update({'text.latex.unicode': True}) #rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

matplotlib.rcParams['font.family'] = 'sans-serif'

MAX_HEIGHT=22
RES = 0.1
SKIP_Z = 1.5
filename = sys.argv[1]
rc, zc, value = np.loadtxt(filename, dtype='float, float, float', delimiter=' ', usecols=(0, 1, 2), unpack=True, skiprows=0)

nx = int(np.amax(rc)/RES + 1)
ny = int(np.amax(zc)/RES + 1)
nylim = int(MAX_HEIGHT/RES)
#ny = min(ny, nylim)
#plt.scatter(rc, zc ,c=value, cmap = plt.cm.jet, s=1)
#plt.hist2d(rc,zc, weights=value, bins=112, cmap = plt.cm.jet)
#Ri = np.arange(0, len(rc))
#Zi = np.arange(0, len(zc))
#R, Z = np.meshgrid(Ri, Zi)

#plt.pcolormesh(X, Y, Matrix)
#yy, xx = np.meshgrid(zc,rc)
#zz = griddata((rc,zc), value, (xx,yy), method='linear')
#plt.pcolor(zz)

#plt.contourf(xx,yy,zz) # if you want contour plot
#plt.imshow(zz)
#Occ=np.array((np.array(rc),np.array(zc),np.array(value)))
data = np.zeros((nylim, nx))
#search for max value above 2m
nbSkip = 2 / RES
maxVal = sys.float_info.min 
for y in range(0, ny):
    if y < nylim:
        for x in range(0, nx):
            ind = x * ny + y
            data[y,x] = 100*value[ind]
            if y > nbSkip and y < ny - nbSkip and data[y,x] > maxVal:
                print (data[y,x], y, ny)
                maxVal = data[y,x]
#print (zc)
#print (rc)
#print (value)
#Z=np.array(((0.1,0.2,0.3,0.4,0.5),(10,1,10,1,10),(1,0,1,0,1)))
#print(Z)
#print(Occ)
fig, ax = plt.subplots(1,1)
#maxVal=100
#img = ax.imshow(data, cmap = plt.cm.jet, origin = "lower", interpolation="bicubic", extent=[min(rc),max(rc),min(zc) + SKIP_Z + 3 ,max(zc)])
img = ax.imshow(data, cmap = plt.cm.jet, origin = "lower", interpolation="bicubic", vmin = 0, vmax=maxVal)
print(maxVal)
ax.set_aspect(1)
fig.colorbar(img).set_label('Occlusion (%)', fontsize=8)
xticks = [0, 0, 2, 4 , 6, 8, 10]
#yticks = [0, 0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20]
locs, labels = plt.yticks()
ylabels = ax.get_yticks().tolist()
yticklabels = []
for lab in ylabels: 
    newtick = float(lab)/10
    newtickstring = str(float(newtick))
    if newtick.is_integer() :
        newtickstring = str(int(newtick))
        
    yticklabels.append(newtickstring)

#yticks = [0, 0, 5, 10, 20, 10, 12.5, 15, 17.5, 20]
ax.xaxis.set_major_locator(plt.MaxNLocator(6))
ax.yaxis.set_major_locator(plt.MaxNLocator(10))
ax.set_xticklabels(xticks)
ax.set_yticklabels(yticklabels)

xlabel = "Distance to the plot center (m)"
ylabel = "Height (m)"

plt.xlabel(xlabel)
plt.ylabel(ylabel);
#plt.xticks(, rc)
#plt.xticks(xticks)
#plt.yticks(yticks)
#plt.xticks(np.arange(len(rc)),rc)
outfile = "/tmp/rzocclu.pdf"
plt.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)


#plt.show()
## Big bins

#f = interp2d(rc,zc,value)
#
#x_coords = np.arange(min(rc),max(zc)+1)
#y_coords = np.arange(min(zc),max(zc)+1)
#Z = f(x_coords,y_coords)
#
#fig = plt.imshow(Z,
#           extent=[min(rc),max(rc),min(zc),max(zc)],
#           origin="lower", cmap = plt.cm.jet)
#plt.colorbar().set_label('Occlusion (%)', fontsize=14)
#
## Show the positions of the sample points, just to have some reference
#fig.axes.set_autoscale_on(False)
#plt.show()
##plt.scatter(rc,zc,400,facecolors='none')

#N = int(len(value)**.5)
#value = value.reshape(N, N)
#plt.imshow(value, extent=(np.amin(rc), np.amax(rc), np.amin(zc), np.amax(zc)),
#        cmap=cm.hot, norm=LogNorm())
