# Difference b/w numpy array copy and view 
import numpy as np
a =np.array([1,2,3,4,5])
b = a.copy()
print(a)
print(b)


import numpy as np
a =np.array([1,2,3,4,5])
b = a.view()
a[0]=23
print(a)
print(b)