import random

def gen_random_list():
    a = []

    for x in range(1000000):
        b = random.randint(0, 1000)
        a.append(b)
    a.sort()

    return a

def bin_search(us_inp):
    while True:
        a = gen_random_list()
        if us_inp in a:
            print('Num is in the list!')
            return True
        else:
            print('Num is not in the list!')
            return False

if __name__ == "__main__":
    us_inp = int(input('Enter a num to check: '))
    bin_search(us_inp)
    
