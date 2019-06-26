import sys
import numpy as np
import pandas as pd
import seaborn as sb

from matplotlib import pyplot as plt
filename = sys.argv[1]
zc, value = np.loadtxt(filename, dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
print zc
data = pd.Series(value,index=zc)
splot = sb.distplot(data,hist=False,vertical=True)
fig = splot.get_figure()

fig.set_size_inches(9, 6)
fig.savefig("xxx.png")
#plt.show()
