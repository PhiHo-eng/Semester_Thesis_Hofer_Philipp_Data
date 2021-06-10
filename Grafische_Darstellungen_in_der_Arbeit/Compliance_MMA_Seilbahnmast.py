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
r = [714199,85730,25871,13478,9222,7365,6670,88679273006,9.71E+17,3.66E+20,645446,2727,2945,3100,3498,4029,4352,4542,4699,4724,4777,4804,4815,4816,4811,4802,4791,4780,4769,4757,4747,4736,4727,4718,4710,4702,4695,4688,4681,4676,4670,4665,4661,4657,4652,4649,4645,4641,4638,4635,4632,4629,4627,4624,4622,4619,4617,4615,4613,4611,4610,4608,4606,4604,4603,4601,4599,4598,4596,4595,4593,4591,4590,4588,4587,4586,4584,4583,4582,4580,4579,4577,4576,4574,4572,4569,4567,4564,4562,4560,4558,4556,4554,4553,4552,4551,4550,4549,4548,4546]

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
plt.plot(t, r, label="Compliance $C$")
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
tikz_save('Compliance_MMA_Seilbahnmast.tex', show_info=False, strict=False,
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
