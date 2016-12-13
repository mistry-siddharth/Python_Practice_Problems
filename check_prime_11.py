def user_inp():
    num = int(input("Please enter a number greater than 2 to check: "))
    return num

def check_prime():
    num = user_inp()
    while num <= 2:
        user_inp()
    for i in range(2, num):        
        if num % i == 0:
            print ('Number is not prime!')
            break
        else:
            print ('Number is prime!')
            break

check_prime()
