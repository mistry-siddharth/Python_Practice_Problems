num = int(input('Enter a number: '))

divlist = range(2, num + 1)
newlist = []

for element in divlist:
    if num % element == 0:
        newlist.append(element)

print (newlist)
