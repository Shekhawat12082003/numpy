#Data type in numpy : i for integer ,b for boolen ,u for unsigned ,f for float ,c for complex float ,m for timedelta , M for datetime   
# O for object ,S for string ,U for unicode string ,V memory

# Checking the data type of numpy array -dtype
import numpy as np
x = np.array([1, 2, 3, 4])
print(x.dtype)

x = np.array(['gagandeep','singh','shekhawat'])
print(x.dtype)

#Creating array with a defined data type :
x = np.array([1, 2, 3, 4],dtype='S')
print(x)
print(x.dtype)

# now we will create an array with data type of 4 bytes int :
x = np.array([1, 2, 3, 4],dtype="i4") # we use i4 for assign 4 byte at intiger 
print(x.dtype)

# converting array in existing array - astype()
x = np.array([1, 2, 3, 4]) # we use i4 for assign 4 byte at intiger
y = x.astype('S') 
print(y.dtype)