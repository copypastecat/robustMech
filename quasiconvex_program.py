import numpy as np
import matplotlib.pyplot as plt
import cvxpy

def D_inf(P_X, Q_X):
    return np.max(np.where(P_X != 0, np.log(P_X / Q_X), 0))

print(D_inf(np.array([0.1, 0.9]),np.array([0.5,0.5])))