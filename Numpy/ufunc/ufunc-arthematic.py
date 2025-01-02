# Arithmetic operators: +,-,*,/
# by using ufunc also takes additional arguments like , where ,dtype and out .
# here now we will use add()

import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.add(x,y)
print (z)

#here now we will use subtract()

import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.subtract(y,x)
print (z)

# here now we wll use multiply()
import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.multiply(x,y)
print (z)


# here now we wll use divide()
import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.divide(y,x)
print (z)

# power() function raises the value from the 1st array to the power of the 2nd array and return the results is a new array .
import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,2,2,2])
z = np.power(x,y)
print (z)

# remainder - we use mod() and remainder() for returning remainder 
import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,2,2,2])
z = np.mod(x,y)
print (z)

import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,2,2,2])
z = np.remainder(x,y)
print (z)

# quotient and mod - we use divmod() function that return both the  quatient and the mod

import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,2,2,2])
z = np.divmod(x,y)
print (z)

