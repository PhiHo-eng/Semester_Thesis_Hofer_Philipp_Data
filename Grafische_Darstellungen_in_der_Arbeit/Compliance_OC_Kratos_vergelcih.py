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
zeta = np.linspace(1, 1, 26)
t =[[]]*len(zeta)
for i, zetai in enumerate(zeta):
    t[i]=i
tEnd = 10
r0 = 0
rd0 = 1

# Calculation
r = [5846,3276,2252,1834,1704,1617,1557,1510,1480,1455,1434,1410,1381,1342,1299,1259,1226,1200,1182,1168,1157,1150,1144,1140,1136,1133]

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
plt.plot(t, r, label="$r(t)$")
plt.xlabel("Iterations")
plt.ylabel("Compliance $C$")
scl.LogScale(r)
           #+
           #"\nveclocity $\\dot{r}$ [m/s]"+
           #"\nacceleration $\\ddot{r}$ [m/s/s]")
plt.xlim((0, 30))
#plt.yscale('log')
sns.despine()
clean_figure()
tikz_save('Compliance_OC_Kratos_vergleich.tex', show_info=False, strict=False,
          extra_axis_parameters={"axis lines*=left",
                                 'height=\\figureheight',
                                 'width=\\figurewidth'})
