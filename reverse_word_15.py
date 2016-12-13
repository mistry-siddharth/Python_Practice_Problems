'''
def string_inp():
    org_a = input('Enter a string: ')
    return org_a
'''

def rev_word():
    org_a = input('Enter a string: ')

    '''
    org_a = string_inp()
    '''

    list_a = org_a.split()
    reverselist_a = list_a[::-1]
    rev_a = ' '.join(reverselist_a)
    return rev_a

print('Reversed string is: ', rev_word())
