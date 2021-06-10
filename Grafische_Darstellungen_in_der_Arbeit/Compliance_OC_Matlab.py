import numpy as np
import matplotlib.pyplot as plt
import matplotlib.scale as scl
import seaborn as sns
from tikzplotlib import save as tikz_save
from tikzplotlib import clean_figure, get_tikz_code
import locale
locale.setlocale(locale.LC_NUMERIC, "de_DE.UTF-8")

# Inputs
m = 100
k = 5
d = 1
zeta = np.linspace(1, 1, 176)
teta = np.linspace(1, 1, 23)
t =[[]]*len(zeta)
td =[[]]*len(teta)
for i, zetai in enumerate(zeta):
    t[i]=i
for i, zetai in enumerate(teta):
    td[i]=i
tEnd = 10


# Calculation
r = [6124.6326,3526.4881,2455.5512 ,2003.7138 ,1851.3501 ,1748.8273 ,1668.2166 ,1604.6715 ,1559.2079 ,1520.5943 ,1474.1748 ,1415.8585 ,1350.7055 ,1287.7743 ,1235.2513 ,1198.8465 ,1173.3751 ,1153.7104 ,1138.9816,1128.2911 ,1118.9739 ,1110.4318,1103.8565 ,1098.8113 ,1095.1314 ,1092.4246 ,1090.2654 ,1088.6284 ,1087.4243,1086.6308 ,1085.7417 ,1084.5333,1083.2070 ,1082.0562 ,1081.2517,1080.6947 ,1080.2878 ,1080.0028 ,1079.8333 ,1079.6913 ,1079.5685 ,1079.4873 ,1079.3433 ,1079.0130 ,1078.5088 ,1078.0605 ,1077.8754 ,1077.7881 ,1077.5552 ,1077.2233 ,1076.8775 ,1076.6098 ,1076.4600 ,1076.3815,1076.2121,1075.7712 ,1075.1420 ,1074.4949 ,1074.0436 ,1073.8473 ,1073.7911,1073.7601 ,1073.7701 ,1073.8448 ,1073.9002,1073.8965 ,1073.7858 ,1073.6542 ,1073.5712 ,1073.4617 ,1073.2859,1073.0228,1072.8208 ,1072.7612 ,1072.7127 ,1072.6460 ,1072.5703 ,1072.4946 ,1072.4004 ,1072.3737 ,1072.3327 ,1072.2838,1072.2548 ,1072.2368 ,1072.2267 ,1072.1976 ,1072.2036 ,1072.2099 ,1072.1918 ,1072.2042 ,1072.2129 ,1072.2425 ,1072.2594 ,1072.2629 ,1072.3028 ,1072.3311,1072.3365 ,1072.3370 ,1072.3538 ,1072.3520 ,1072.3413 ,1072.3436 ,1072.3105 ,1072.2931 ,1072.2706 ,1072.2675 ,1072.2592,1072.2591 ,1072.1881 ,1072.0687 ,1071.9782 ,1071.9353 ,1071.9441 ,1071.9431 ,1071.9403 ,1071.9201 ,1071.8157,1071.6701,1071.4877,1071.4265,1071.4075,1071.3595,1071.3356,1071.3219,1071.3104,1071.2932,1071.2837,1071.2549,1071.2069 ,1071.0944,1070.9825,1070.9468 ,1070.9563 ,1070.9562 ,1070.9470 ,1070.9563 ,1070.9559 ,1070.9480,1070.9591,1070.9389 ,1070.9426,1070.9415 ,1070.9619 ,1070.9503,1070.9371 ,1070.9207 ,1070.9020 ,1070.8929 ,1070.8595 ,1070.8403,1070.8009 ,1070.7566 ,1070.6212,1070.4205,1070.2631 ,1070.2213,1070.1898 ,1070.1352 ,1070.1052 ,1070.0923,1070.0441 ,1070.0131 ,1069.9718,1069.9464 ,1069.9124,1069.8924 ,1069.8384 ,1069.8031,1069.7769,1069.7360,1069.6849,1069.6481,1069.6223 ,1069.6070 ,1069.5808 ,1069.5803 ]

rd = [5846,3276,2252,1834,1704,1617,1557,1510,1480,1455,1434,1410,1381,1342,1299,1259,1226,1200,1182,1168,1157,1150,1144]


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
fig, ax = plt.subplots(figsize=(5, 5))
# Plot
plt.plot(t, r, label="Compliance $C$ with Matlab")
plt.plot(td, rd, label="Compliance $C$ with Kratos")

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
plt.xlim((0, 90))
#plt.yscale('log')
sns.despine()
clean_figure()
tikz_save('Compliance_OC_Matlab.tex', show_info=False, strict=True,
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
