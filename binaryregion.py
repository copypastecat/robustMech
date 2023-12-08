import numpy as np
import matplotlib.pyplot as plt

def compute_epsPML(P_X,P):
    P_Y = np.inner(P_X,P.transpose())
    ell_0 = np.log(np.max(P[:,0]/P_Y[0]))
    ell_1 = np.log(np.max(P[:,1]/P_Y[1]))
    return np.max([ell_0,ell_1])

def eval_epsPML(P_X,epsilon,P):
    ell = compute_epsPML(P_X,P)
    boolean_return = None
    if(ell <= epsilon):
        boolean_return = 1
    else:
        boolean_return = 0
    
    return boolean_return 

stepsize = 0.005
range = int(1/stepsize)
grid = np.ones(shape=(range,range))

for p in np.arange(0,1,0.01):
    P_X = np.array([p,1-p])
    epsilon = np.log(1.5)
    #'''

    for (index1,p_11) in enumerate(np.arange(0.001,1,stepsize)):
        for (index2,p_21) in enumerate(np.arange(0.001,1,stepsize)):
            P = np.array([[p_11, 1-p_11],[p_21, 1-p_21]])  
            grid[index1,index2] = grid[index1,index2]*eval_epsPML(P_X,epsilon,P)

    #'''
plt.imshow(grid)
plt.show()
'''
t = compute_epsPML(P_X,np.array([[0.1,0.9],[0.1,0.9]]))
print(t)
'''

   