def reverse_words(str):
    #go for it
    '''
    new_str = str.split()
    final_list = []
    final_str = ''
    for x in new_str:
        word = x[::-1]
        final_list.append(word)

    final_str = ' '.join(final_list)
    return(final_str)
    '''
    return ' '.join(s[::-1] for s in str.split(' '))

print(reverse_words('elbuod decaps sdrow'))
