# prem - df(degree of freedom), size 
from numpy import random 
x = random.chisquare(df=2,size=(2,3))
print(x)

# visualization of chisquare dist

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

x = random.chisquare(df=2,size=1000) 
sns.kdeplot(x)
plt.show()
