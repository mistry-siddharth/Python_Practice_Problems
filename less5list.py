mylist = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
num = int(input('Enter a number: '))
newlist = []

for element in mylist:
    if element < num:
        newlist.append(element)

print (newlist)
