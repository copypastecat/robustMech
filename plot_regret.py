import numpy as np
import matplotlib.pyplot as plt
from math import *

def D_inf(P,Q):
    if(np.any(Q[0]) <= 0):
        Q[0] = 0.001
    if(np.any(Q[1]) <= 0):
        Q[1] = 0.001
    if(np.any(Q[2]) <= 0):
        Q[2] = 0.001                
    log_ratio = np.log(np.divide(P,Q))
    D = np.max(log_ratio)
    return D


def evaluate_worst_case_regret(p):
    maxD = 0
    q = np.arange(0,0.1,0.01)
    for q1 in q:
        q_sub = q[q-q1 <= 1]
        for q2 in q_sub:
            q_subsub = q_sub[q_sub-q2 <= 1]
            q3 = 1-q1-q2    
            Q = [q1,q2,q3]
            D = D_inf(p,Q)
            if(D > maxD):
                maxD = D
                print(Q)
    return maxD


#p = np.arange(0,1,0.1)
#min_wcr = 100
#for p1 in p:
#    p_sub = p[p-p1 <= 1]
#    for p2 in p_sub:
#        p3 = 1-p1-p2
#        P = [p1,p2,p3]
#        r = evaluate_worst_case_regret(P)
#        if(r < min_wcr):
#            min_wcr = r
#            print(r)
#            print(P)

wcr = evaluate_worst_case_regret([0.2,0.4,0.4])
print(wcr)