from numpy import random
a = random.randint(100)
print(a) 

# you can also generate float() via rand()
a = random.rand()
print(a) 

#  You can also generate random Array .
# 1-D array
a = random.randint(100,size=(5))
print(a) 

# 2-D array
a = random.randint(100,
size=(3,5))
print(a) 


# you can also generate random number from an array 
# choice()
# 1-D array
a = random.choice([3,5,7,6,4,9])
print(a) 