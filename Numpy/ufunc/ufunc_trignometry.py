# NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
import numpy as np
x = np.sin(np.pi/2)
print(x)

import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

# By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
# Degrees Into Radians

import numpy as np
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# Radians to Degrees

import numpy as np
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

# Angles of Each Value in Arrays

import numpy as np
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

# Hypotenues - NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.

import numpy as np
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)