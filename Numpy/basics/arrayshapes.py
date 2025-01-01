import numpy as np 
a = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(a.shape)

# reshaping of an array
#1d to 2d
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(3,4)
print(b)

# Reshaping 1d to 3d 
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(2,3,2)
print (b)
print(b.ndim)

# unknown Dimension 
a = np.array([1,2,3,4,5,6,7,8])
b = a.reshape(2,2,-1)
print(b)