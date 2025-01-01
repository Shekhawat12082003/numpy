import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c =np.concatenate((a,b))
print(c)

# joining in 2d
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c =np.concatenate((a,b),axis=1)
print(c)

# Joining array using stack function

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c =np.stack((a,b),axis=1)
print(c)

# Stacking along with rows with hstack() function 
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c =np.hstack((a,b))
print(c)

# Stacking along with column with stack() function 
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c =np.vstack((a,b))
print(c)