# normal(gaussian) distribution - very important 
# random.normal()- loc(mean),scale(standard deviation),size 
 
# we are generating a random normal distribution of size 2*3
from numpy import random
a = random.normal(size=(2,3))
print(a)

from numpy import random
a = random.normal(loc=1,scale=2,size=(2,3))
print(a)


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000),hist=False)
plt.show() 