# metplotlib(pyplot) -- seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Distplot -distribution plot
sns.distplot([0,1,2,3,4,5])
plt.show()
# plotting a displot without histogram
import matplotlib.pyplot as plt
import seaborn as sns
# Distplot -distribution plot
sns.distplot([0,1,2,3,4,5],hist = False)
plt.show()