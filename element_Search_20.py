import random

def gen_random_list():
    a = [random.randint(0, 30) for x in range(10)]
    a.sort()
    return a

'''
def bin_search(us_inp):
    while True:
        a = gen_random_list()
        center_pt = int(len(a)/2)

        if us_inp < a[center_pt]:
            less_than_a = a[0:center_pt]
            if us_inp in less_than_a:
                print('Num is in the list!')
                return True
            else:
                print('Num is not in the list!')
                return False
        else:
            greater_than_a = a[center_pt:len(a)]
            if us_inp in greater_than_a:
                print('Num is in the list!')
                return True
            else:
                print('Num is not in the list!')
                return False
'''

def bin_search(arr, us_inp):
    if len(arr) < 1:
        return False

    mid_pt = len(arr)//2
    if arr[mid_pt] == us_inp:
        return True

    if len(arr) == 1:
        return False

    if arr[mid_pt] > us_inp:
        return bin_search(arr[0:mid_pt], us_inp)

    if arr[mid_pt] < us_inp:
        return bin_search(arr[mid_pt:len(arr)], us_inp)
    
if __name__ == "__main__":
    arr = gen_random_list()
    print(arr)
    us_inp = int(input('Enter a num to check: '))
    print(bin_search(arr, us_inp))
    
