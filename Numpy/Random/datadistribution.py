   # 1-D array
from numpy import random
a = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0],size=(100)) # p  use for probability
print(a) 

# 2-D array
from numpy import random
a = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0],size=(3,5)) # p  use for probability
print(a) 