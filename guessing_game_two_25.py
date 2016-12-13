'''
def iter_guess_num():
    left = 0
    right = 100
    guess = (left + right)//2
    guess_cntr = 0

    print('Is', guess, 'correct, high or low? ')
    us_inp = input()
    
    while us_inp != 'correct':
        if us_inp == 'high':
            right = guess
            guess_cntr += 1
        elif us_inp == 'low':
            left = guess
            guess_cntr += 1
        elif us_inp == 'exit':
            break

        guess = (left + right)//2

        print('Is', guess, 'correct, high or low? ')
        us_inp = input()
            
    else:
        print('You guessed right after', guess_cntr, 'trials!')            

if __name__ == '__main__':
    print('Hey computer read my mind!')
    iter_guess_num()
'''

def rec_guess_num(left, right, guess_cntr):

    guess = (left + right)//2
    print('Is', guess, 'correct, high or low? ')
    us_inp = input()

    if us_inp == 'c':
        print('You guessed correctly after', guess_cntr, 'trials!')
        return True
    if us_inp == 'h':
        right = guess
        guess_cntr += 1
        return (rec_guess_num(left, right, guess_cntr))
    if us_inp == 'l':
        left = guess
        guess_cntr += 1
        return (rec_guess_num(left, right, guess_cntr))

if __name__ == "__main__":
    guess_cntr = 0
    rec_guess_num(0, 100, guess_cntr)
