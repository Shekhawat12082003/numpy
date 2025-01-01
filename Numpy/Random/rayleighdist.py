from numpy import random
x= random.rayleigh(scale=2,size=(2,4))
print(x)

# visualization of reyleigh
from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 
x= random.rayleigh(scale=2,size=(2,4))
sns.kdeplot(x)
plt.show()