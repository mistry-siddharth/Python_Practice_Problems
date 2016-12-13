import math

def datainp():
    global num
    num = input('Enter a number: ')

def calcoddeven():
    global mod
    mod = int(num) % 2
    if mod == 0:
        print('This is an even number!\n')
    else:
        print('This is an odd number!\n')

while True:
    datainp()

    if num.isdigit():
        calcoddeven()
    else:
        print('Please enter a number value!\n')
        datainp()
        calcoddeven()
