from numpy import random
x = random.uniform(size=(2,4))
print(x)

# vizualization of uniform dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.uniform(size=1000)
sns.kdeplot(x)
plt.show()
