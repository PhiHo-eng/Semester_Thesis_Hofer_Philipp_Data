import numpy as np
import matplotlib.pyplot as plt
import matplotlib.scale as scl
import seaborn as sns
from tikzplotlib import save as tikz_save
from tikzplotlib import clean_figure, get_tikz_code

# Inputs
m = 100
k = 5
d = 1
zeta = np.linspace(1, 1, 100)
t =[[]]*len(zeta)
for i, zetai in enumerate(zeta):
    t[i]=i
tEnd = 10
r0 = 0
rd0 = 1

# Calculation
r = [0.15,0.27,0.315,0.317,0.31,0.29,0.27,0.26,0.25,0.39,0.53,0.62,0.5,0.4,0.36,0.31,0.27,0.26,0.24,0.23,0.22,0.21,0.206,0.2,0.195,0.19,0.186,0.183,0.1795,0.177,0.175,0.173,0.171,0.169,0.168,0.167,0.166,0.165,0.164,0.163,0.1627,0.162,0.1616,0.1612,0.1607,0.1604,0.16,0.1598,0.1594,0.1593,0.159,0.1588,0.1586,0.1585,0.1583,0.1581,0.1579,0.1578,0.1577,0.1575,0.1574,0.1573,0.1572,0.1571,0.157,0.1569,0.1568,0.1567,0.1566,0.1565,0.1564,0.1564,0.1563,0.1562,0.1561,0.156,0.1559,0.1599,0.1558,0.1557,0.1556,0.1555,0.1554,0.1553,0.1551,0.1549,0.1548,0.1547,0.1545,0.1544,0.1542,0.1541,0.154,0.1538,0.1537,0.1535,0.1534,0.1533,0.1532,0.1531]
#r = [r0]
#rd = [rd0]
#rdd = []
#for i in range(int(tEnd/dt)):
#    rdd.append(-d/m*rd[-1]-k/m*r[-1])
#    rd.append(rd[-1]+rdd[-1]*dt)
#    r.append(r[-1]+rd[-2]*dt)
#rdd.append(-d/m*rd[-1]-k/m*rd[-1])
#t = np.linspace(0, tEnd, int(tEnd/dt+1))

# Plot
plt.plot(t, r, label="Volume fraction $g_{comp}$")
plt.xlabel("Iterations")
plt.ylabel("Volume fraction $g_{comp}$")
scl.LogScale(r)
           #+
           #"\nveclocity $\\dot{r}$ [m/s]"+
           #"\nacceleration $\\ddot{r}$ [m/s/s]")
plt.xlim((0, 100))
#plt.yscale('log')
sns.despine()
clean_figure()
tikz_save('Constrain_MMA_Seilbahnmast.tex', show_info=False, strict=False,
          extra_axis_parameters={'height=\\figureheight',
                                 'width=\\figurewidth',
                                 "separate axis lines",
                                 "enlargelimits=false",
                                 "line cap=round",
                                 "clip=false",
                                 "axis lines*=left",
                                 "axis x line shift=10pt",
                                 "axis y line shift=10pt",
                                 "xlabel shift=10pt",
                                 "ylabel shift=10pt",
                                 "scaled ticks=false",
                                 "tick align=outside",
                                 'y tick label style={xshift=-32}',
                                 'ylabel shift= 20pt',
                                 'ylabel style={xshift=-40}',
                                 'ylabel style={yshift=20}',
                                 'x tick label style={yshift=-8}',
                                ' xlabel style={yshift=-10}'})