import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

'''for exporting PGF code
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
'''
#p = [0.25,0.25,0.25,0.25] 
p=[0.6,0.4]

eps_max = -np.log(np.min(p))
p_min = np.min(p)

exp_eps = np.arange(1,1/(1-p_min),0.001)
U1 = []
L1 = []
L2 = []

for eps in exp_eps:
    eps_u = np.log(eps)
    eps_l = np.log((1/(1-eps*(1-p_min))))-eps_max
    eps_lu = np.log((1-p_min)/(1-eps*p_min)) 
    U1.append(eps_u)
    L1.append(eps_l)
    L2.append(eps_lu)

"""
p = [0.25,0.25,0.25,0.25]
eps_max = -np.log(np.min(p))
p_min = np.min(p)
U2 = []
L2 = []

for eps in exp_eps:
    eps_u = np.log(eps)
    eps_l = np.log((1/(1-eps*(1-p_min))))-eps_max
    U2.append(eps_u)
    L2.append(eps_l)
"""

plt.plot(U1,L1)
plt.plot(U1,L2)
plt.plot(U1,U1,color="green")
#plt.plot(U2,L2)
#plt.legend(["non-uniform","uniform"])
plt.vlines([np.log(1/(1-p_min))],ymin=0,ymax=3,linestyles='dashed',colors='k')
plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,np.log(1/(1-p_min))],["0","0.1","0.2","0.3","0.4","0.5","0.6","$\log \\frac{1}{(1-0.5)}$"])
plt.ylim((0,1.6))
plt.xlabel("$\epsilon_u$")
plt.ylabel("$\epsilon_l$")
plt.fill_between(U1, L1, 12, color='dimgray' , alpha=.2)
plt.fill_between(U1,L2,0,color='gray', alpha=.5)
#plt.fill_between(U1,L1,L2,color='lightsteelblue',alpha=.3)
plt.annotate("implied by $\epsilon_u$-PML",(0.05,1))
plt.annotate("implied by lower-bound only", (0.165,0.01))
plt.annotate("implied by lower-bound only", (0.3,0.1))
#plt.annotate("both bounds achievable", (0.155,0.5))
#plt.annotate("$\epsilon_u$-LIP",xy=(0.23,0.35),xytext=(0.15,3),arrowprops=dict(facecolor='black', shrink=0.02))
#plt.annotate("$\epsilon_u$-PML",xy=(0.27,3),xytext=(0.2,4),arrowprops=dict(facecolor='black', shrink=0.02))
#plt.legend(["$\epsilon_u$-PML (only upper bound)", "only lower bound", "$\epsilon_u$-LIP"])
plt.legend(["$\epsilon_u$-PML (both bounds tight)","$\epsilon_u$-LIP (only lower bound tight)"])
plt.tight_layout()
#plt.savefig('ALIPfromPML_binary.svg')
plt.show()

