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
p = [0.25,0.25,0.25,0.25] 

eps_max = -np.log(np.min(p))
p_min = np.min(p)

exp_eps = np.arange(1,1/(1-p_min),0.00001)
U1 = []
L1 = []

for eps in exp_eps:
    eps_u = np.log(eps)
    eps_l = np.log((1/(1-eps*(1-p_min))))-eps_max
    U1.append(eps_u)
    L1.append(eps_l)

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
plt.plot(U1,U1)
#plt.plot(U2,L2)
#plt.legend(["non-uniform","uniform"])
plt.vlines([np.log(1/(1-p_min))],ymin=0,ymax=12,linestyles='dashed',colors='k')
plt.xticks([0,0.1,0.2,np.log(1/(1-p_min))],["0","0.1","0.2","$\log 1/(1-p_{min})$"])
plt.xlabel("$\epsilon_u$")
plt.ylabel("$\epsilon_l$")
plt.fill_between(U1, L1, 12, color='dimgray' , alpha=.2)
plt.fill_between(U1,L1,0,color='gray', alpha=.5)
plt.annotate("upper bound tight",(0.1,7))
plt.annotate("l. b. tight", (0.24,1))
plt.annotate("$\epsilon_u$-LIP",xy=(0.23,0.35),xytext=(0.15,3),arrowprops=dict(facecolor='black', shrink=0.02))
plt.annotate("$\epsilon_u$-PML",xy=(0.27,3),xytext=(0.2,4),arrowprops=dict(facecolor='black', shrink=0.02))
plt.tight_layout()
#plt.savefig('ALIPfromPML.svg')
plt.show()

