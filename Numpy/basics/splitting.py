import numpy as np
#array_split()
# Stacking along with rows with hstack() function 
a = np.array([1,2,3,4,5,6 ])
b = np.array_split(a,3)
print(b)

# Now we will split this array in 4 parts  
a = np.array([1,2,3,4,5,6 ])
b = np.array_split(a,4)
print(b)