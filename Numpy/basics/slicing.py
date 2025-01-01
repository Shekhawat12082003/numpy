# slicing in array  
import numpy as np 
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[1:5])
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[4:])

a = np.array([1,2,3,4,5,6,7,8,9])
print(a[1:5:2])

# negative slicing 
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[-8:-4])
