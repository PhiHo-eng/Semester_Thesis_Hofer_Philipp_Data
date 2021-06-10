import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tikzplotlib import save as tikz_save
from tikzplotlib import clean_figure, get_tikz_code

# Inputs
m = 100
k = 5
d = 1
zeta = np.linspace(1, 1, 7)
t =[[]]*len(zeta)
for i, zetai in enumerate(zeta):
    t[i]=i
tEnd = 10
r0 = 0
rd0 = 1

# Calculation
r = [0.15, 0.3075, 0.4875, 0.6675, 0.845, 0.999, 1]

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
           #+
           #"\nveclocity $\\dot{r}$ [m/s]"+
           #"\nacceleration $\\ddot{r}$ [m/s/s]")
plt.xlim((0, 8))
ymax = np.max([np.max(np.abs(r))])
plt.ylim((0, 1))
#plt.legend(frameon=False)
sns.despine()
clean_figure()
tikz_save('Vol_frac_steigend.tex', show_info=False, strict=False,
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
