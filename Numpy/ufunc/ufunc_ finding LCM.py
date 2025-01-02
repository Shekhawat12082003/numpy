# The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
import numpy as np 
a = 4
b = 6 
x = np.lcm(a,b)
print(x)


# Finding LCM in Arrays
# To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)