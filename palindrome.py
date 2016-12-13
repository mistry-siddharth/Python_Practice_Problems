'''
inpstring = input('Enter a string to check: ')

reversestring = inpstring[::-1]

if inpstring == reversestring:
    print ('Entered string is a palindrome!')
else:
    print ('Entered string is not a palindrome!')
'''
def is_palindrome(word):

    letters = list(word)
    is_palindrome = True
    i = len(letters)

    for letter in letters:
        if letter == letters[i-1]:
            i -= 1
            #letters.pop(-1)
        else:
            is_palindrome = False
            break

    return is_palindrome

print(is_palindrome('civic'))
