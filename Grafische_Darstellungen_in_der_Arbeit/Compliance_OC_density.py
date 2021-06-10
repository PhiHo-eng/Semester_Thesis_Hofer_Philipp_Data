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
teta = np.linspace(1, 1, 28)
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

rd = [5846,3268,2256,1861,1750,1681,1629,1593,1569,1549,1535,1522,1512,1500,1491,1475,1457,1437,1410,1382,1352,1323,1300,1284,1271,1262,1254,1251]
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
plt.plot(t, r, label="Compliance $C$ wtihout density filter")
plt.plot(td, rd, label="Compliance $C$ wtih density filter")

plt.xlabel("Iterations")
plt.ylabel("Compliance $C$")
scl.LogScale(r)
plt.legend()
           #+
           #"\nveclocity $\\dot{r}$ [m/s]"+
           #"\nacceleration $\\ddot{r}$ [m/s/s]")
plt.xlim((0, 30))
#plt.yscale('log')
sns.despine()
clean_figure()
tikz_save('Compliance_OC_density.tex',  show_info=False, strict=False,
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
                                 'y tick label style={xshift=-27}',
                                 'ylabel shift= 20pt',
                                 'ylabel style={xshift=-40}',
                                 'ylabel style={yshift=15}',
                                 'x tick label style={yshift=-8}',
                                ' xlabel style={yshift=-10}'})