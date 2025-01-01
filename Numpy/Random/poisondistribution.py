# poison distribution - it estimates how many times an event can happen
# parm - lam(NUMBER OF Accuranve),size
from numpy import random
a = random.poisson(lam=2,size=10)
print(a)
# visualization of binomial  dist
import matplotlib.pyplot as plt
import seaborn as sns 
sns.distplot(random.poisson(lam=2,size=1000),kde=False)
plt.show()

# presenting both the plots in some figure normal and possn dist
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
 
sns.distplot(random.normal(loc=50,scale=7,size=1000),hist=False,label='normal')
sns.distplot(random.poisson(lam=50,size=1000),hist=False,label = 'poisson')
plt.show()