#ufanc - stands for universal function and they are actually numpy functions tht operates on the ndarray objects.

# ufunc- also takes additional arguments like ,where, dtype and out .

# vectorization - converting the iterating statement into a vector based statement .

# example without ufanc - zip()
x=[1,2,3,4]
y=[5,6,7,8]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)

# with ufac ,we will now use add()
import numpy as np
x=[1,2,3,4]
y=[5,6,7,8]
z=np.add(x,y)
print(z)


# with ufac ,we will now use subtract()
import numpy as np
x=[1,2,3,4]
y=[5,6,7,8]
z=np.subtract(x,y)
print(z)