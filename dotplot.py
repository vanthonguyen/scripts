import sys
import os
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()

filename = sys.argv[1]
title = ""
xlabel = ""
ylabel = "z"
if len(sys.argv) > 2 :
    title = sys.argv[2]
if len(sys.argv) > 3 :
    xlabel = sys.argv[3]
if len(sys.argv) > 4 :
    ylabel = sys.argv[4]
zc, value = np.loadtxt(filename, dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
ax.plot(value, zc, 'ro')
#data = pd.Series(value,index=zc)
#splot = sb.distplot(data,hist=False,vertical=True)
#fig = splot.get_figure()
#

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel);

fig.set_size_inches(9, 6)
base = os.path.splitext(filename)[0]
outfile = base + "-dot.pdf"
fig.savefig(outfile)
#plt.show()
