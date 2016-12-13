import random

a = random.sample(range(50), 7)
b = random.sample(range(30), 11)

result = [i for i in set(a) if i in b]

print (a)
print (b)
print (result)
