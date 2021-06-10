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
zeta = np.linspace(1, 1, 84)
teta = np.linspace(1, 1, 84)
t =[[]]*len(zeta)
td =[[]]*len(teta)
for i, zetai in enumerate(zeta):
    t[i]=i
for i, zetai in enumerate(teta):
    td[i]=i
tEnd = 10
r0 = 0
rd0 = 1

# Calculation
r = [714199,58944,37108,20361,13325,9511,7570,6392,5733,5360,5153,5027,4946,4896,4854,4818,4781,4754,4733,4712,4698,4679,4666,4648,4637,4622,4609,4595,4580,4566,4548,4529,4512,4495,4483,4473,4465,4459,4458,4455,4452,4452,4448,4449,4447,4448,4447,4445,4444,4447,4443,4445,4443,4445,4444,4445,4444,4445,4443,4440,4438,4431,4430,4427,4425,4424,4424,4421,4421,4420,4418,4418,4417,4414,4415,4414,4411,4411,4410,4408,4408,4407,4404,4404]


#rd = [0.15,0.2629,0.1743,0.1557,0.1499,0.15,0.1499,0.15,0.1499,0.15,0.1499,0.1499,0.15,0.1499,0.15,0.1499,0.1499,0.1499,0.1499,0.15,0.1499,0.15,0.1499,0.15,0.149,0.1499,0.15,0.15,0.15,0.1499,0.1499,0.15,0.15,0.15,0.1499,0.1499,0.1499,0.15,0.1499,0.1499,0.1499,0.1499,0.15,0.15,0.15,0.1499,0.1499,0.15,0.15,0.1499,0.15,0.1499,0.15,0.1499,0.15,0.1499,0.15,0.1499,0.1499,0.15,0.15,0.15,0.1499,0.1499,0.15,0.15,0.1499,0.15,0.15,0.1499,0.15,0.15,0.1499,0.15,0.1499,0.1499,0.15,0.1499,0.1499,0.15,0.15,0.1499,0.15,0.15]
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
plt.plot(t, r, label="Compliance $C$ with OC")
#plt.plot(td, rd, label="$Constrain$ $value$")
plt.xlabel("Iterations")
plt.ylabel("Compliance $C$")

scl.LogScale(r)
           #+
           #"\nveclocity $\\dot{r}$ [m/s]"+
           #"\nacceleration $\\ddot{r}$ [m/s/s]")
plt.xlim((0, 100))
plt.yscale('log')
sns.despine()
clean_figure()
tikz_save('Compliance_OC_Seilbahnmast.tex', show_info=False, strict=False,
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
