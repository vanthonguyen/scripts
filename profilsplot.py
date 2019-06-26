import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc

plt.style.use('seaborn-whitegrid')


matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rcParams.update({'text.latex.unicode': True})
#rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})
matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure()
ax = plt.axes()

filename1 = sys.argv[1]
zc, value = np.loadtxt(filename1, dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
ax.plot(value, zc, label="Scan 0")

#filename2 = sys.argv[2]
#filename3 = sys.argv[2]

title = ""
xlabel = "PAD"
ylabel = "z (m)"
if len(sys.argv) > 2 :
    filename2 = sys.argv[2]
    zc2, value2 = np.loadtxt(filename2, dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    ax.plot(value2, zc2, label="Scan 1 2 3 4")
if len(sys.argv) > 3 :
    filename3 = sys.argv[3]
    zc3, value3 = np.loadtxt(filename3, dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    ax.plot(value3, zc3, label="Scan 0 1 2 3 4")
#data = pd.Series(value,index=zc)
#splot = sb.distplot(data,hist=False,vertical=True)
#fig = splot.get_figure()
#

if len(sys.argv) > 4 :
    title = sys.argv[4]

ax.legend()
ax.set_ylim(0, 15)
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel);

fig.set_size_inches(6, 9)
base = os.path.splitext(filename1)[0]
outfile = base + "multi.pdf"
fig.savefig(outfile)
#plt.show()
