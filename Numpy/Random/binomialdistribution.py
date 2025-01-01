# binomial distribution - Discrete distributin - binary output
# param - n(numbers of trials),p(probability),size(shape) 
from numpy import random
a =random.binomial(n=10,p=0.5,size=10)
print(a)

# visualization of binomial  dist
import matplotlib.pyplot as plt
import seaborn as sns 
sns.distplot(a,hist=False)
plt.show()