#ittrating array
import numpy as np
a=np.array([1,2,3])
for i in a:
    print(i)


a=np.array([[1,2,3],[4,5,6]])
for i in a:
    print(i)

#itterate in each element 
a=np.array([[1,2,3],[4,5,6]])
for i in a:
    for j in i:
        print(j) 

# Iterating array using the nditer() function

a=np.array([[[1,2,],[3,4],[5,6],[7,8]]])
for i in np.nditer(a):
    print(i)
