import numpy as np

A = np.array([3,4])

v = np.array([-1,4])

B = A + -3 * v

print(B)

M = np.array([[3,3],[4,4],[5,5],[5,9]])
N = np.array([[3,4,6],[5,6,7]])
print(M.shape)

O = np.dot(M,N)

print(O) 
print(O.shape)
#np.dot -> multiplikation