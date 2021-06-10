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
zeta = np.linspace(1, 1, 23)
teta = np.linspace(1, 1, 33)
t =[[]]*len(zeta)
td =[[]]*len(teta)
for i, zetai in enumerate(zeta):
    t[i]=i
for i, zetai in enumerate(teta):
    td[i]=i
tEnd = 10
rd0 = 1

# Calculation
r = [5846,3276,2252,1834,1704,1617,1557,1510,1480,1455,1434,1410,1381,1342,1299,1259,1226,1200,1182,1168,1157,1150,1144]

rd = [5846,4420,3412,2768,2348,2063,1901,1804,1728,1680,1651,1623,1597,1563,1532,1497,1462,1437,1400,1382,1336,1296,1259,1231,1215,1204,1195,1188,1179,1171,1163,1157,1153]

#r = [r0]
#rd = [rd0]
#rdd = []
#for i in range(int(tEnd/dt)):
#    rdd.append(-d/m*rd[-1]-k/m*r[-1])
#    rd.append(rd[-1]+rdd[-1]*dt)
#    r.append(r[-1]+rd[-2]*dt)
#rdd.append(-d/m*rd[-1]-k/m*rd[-1])
#t = np.linspace(0, tEnd, int(tEnd/dt+1))
fig, ax = plt.subplots(figsize=(5, 5))
# Plot
plt.plot(t, r, label="Compliance $C$ with OC")
plt.plot(td, rd, label="Compliance $C$ with MMA")

ax.spines['bottom'].set_bounds(min(r), max(r))
ax.spines['left'].set_bounds(np.min((zeta)), np.max((zeta)))
ax.spines['right'].set_bounds(min(rd), max(rd))

plt.xlabel("Iterations")
plt.ylabel("Compliance $C$")
scl.LogScale(r)
plt.legend()
           #+
           #"\nveclocity $\\dot{r}$ [m/s]"+
           #"\nacceleration $\\ddot{r}$ [m/s/s]")
plt.xlim((0, 35))
#plt.yscale('log')
sns.despine()
clean_figure()
tikz_save('Compliance_OC_MMA.tex', show_info=False, strict=False,
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
                                 'ymajorgrids',
                                 'x tick label style={yshift=-8}',
                                ' xlabel style={yshift=-10}'})
