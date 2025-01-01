# param - n(number of possibility or outcomes ), pvals(list of possibility or outcomes),size
from numpy import random

a = random.multinomial(n=4,pvals=[ 1/6,1/6,1/6,1/6,1/6,1/6])
print(a)

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(a,hist=False)
plt.show()