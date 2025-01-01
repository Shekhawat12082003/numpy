from numpy import random
x = random.zipf(a=5,size=(2,3))
print(x)

# visualization of zipf dist
from matplotlib import pyplot as plt
import seaborn as sns 
sns.kdeplot(x)
plt.show()