# To create your own ufunc ,you have to define a function , like you add it to the numpy function with frompyfunc() method
# argument of frompyfunc(): function , inputs , outputs

import numpy as np 
def myadd(x,y):
    return x+y
myadd = np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[5,6,7,8]))
