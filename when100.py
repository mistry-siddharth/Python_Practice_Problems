import datetime

now = datetime.datetime.now()
currentyear = now.year

def datainp():
    global age, name
    name = input('What is your name? ')
    age = input('What is your age? ')

def yearcalc():
    when100 = currentyear - int(age) + 100
    print("You'll be 100 years of age in",when100,'\n')

while True:
    datainp()
    if age.isdigit():
        yearcalc()
    else:
        print('You did not enter a number. Please enter a number!\n')
        datainp()
        yearcalc()
