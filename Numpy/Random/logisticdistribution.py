# param - loc(mean-0),scale(standard deviation ,1),size
from numpy import random

a = random.logistic(loc=1,scale=2,size=(2,3))
print(a)
# visualization of logistic dist
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(a,hist=False)
plt.show()