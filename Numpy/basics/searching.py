#searching array-by using where()
import numpy as np
a = np.array([1,3,7,3,5,2])
b= np.where(a==3)
print(b)


# now we we will find the even numbers 
a = np.array([1,2,3,4,5,6,7,8])
b= np.where(a%2==0)
print(b)

# now we we will find the odd numbers 
a = np.array([1,2,3,4,5,6,7,8])
b= np.where(a%2==1)
print(b)

# Searchsorted() - perform binary search in array.
a = np.array([5,6,7,8])
b= np.searchsorted(a,7)
print(b)

#sort()
a = np.array([1,2,5,8,5,7,8])
b= np.sort(a)
print(b)


