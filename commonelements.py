import random

a = []
for i in range(7):
    a.append(random.randrange(1,100))

b = []
for i in range(10):
    b.append(random.randrange(1,50,4))

print (a)
print (b)

newlist = []

for element in a:
    if element in b:
        newlist.append(element)

newlist = list(set(newlist))
        
print (newlist)
