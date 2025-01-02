#  trunction - trunc() function remove the decimal and return closest to zero 
import numpy as np
a = np.array([1.2343, 2.66678])
b = np.trunc(a)
print(b)

# fix() same as trunc() function 
import numpy as np
a = np.array([1.1666, 2.66678])
b = np.fix(a)
print(b)

# Rounding - the around() function increment preciding digit or decimal 
import numpy as np
a = np.array([1.1666, 2.66678])
b = np.around(a)
print(b)

# floor() round off decimal to nearest lower integer 
import numpy as np
a = np.array([1.1666, 2.66678])
b = np.floor(a)
print(b)

# ceil() - rounding off to the nearest upper integers 
import numpy as np
a = np.array([1.2343, 2.66678])
b = np.ceil(a)
print(b)
