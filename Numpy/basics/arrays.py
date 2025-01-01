import numpy as np
x = np.array([1, 2, 3, 4, 5])
print(x)
print(type(x))

#using tuples
y =np.array((1,2,3,4,5,6))
print(y)
print(type(y))

# dimension in array - a dimension in a array is one level of array depth

# 0-d array
x =np.array(42)
print(x)

# 2-d array
two = np.array([[1,2,3] , [1,2,3]])
print(two)

# check how many dimensions the array have : ndim attribute 
x = np.array([1, 2, 3, 4, 5])
y =np.array((1,2,3,4,5,6))
two = np.array([[1,2,3] , [1,2,3]])

print(x.ndim)
print(y.ndim)
print(two.ndim)
