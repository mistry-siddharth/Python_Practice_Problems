#iterative method

'''
def fibonacci():
    endpt = int(input('Enter end point for the series: '))

    count = 2
    i = 0
    fib = [1, 1]
    
    while count < endpt:
        fib.append(fib[count-1] + fib[count-2])
        count += 1

    return fib

print(fibonacci())
'''

#recursive method

def arr(n):
    arr = [fibonacci(x) for x in range(1, n+1)]
    return arr

def fibonacci(n):
    if n <= 0:
        print('Wrong!')

    #base case
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    us_inp = int(input('Enter end point for the series: '))
    print(arr(us_inp))
