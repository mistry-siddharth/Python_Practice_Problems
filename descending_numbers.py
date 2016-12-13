def Descending_Order(num):
    #Bust a move right here
    s = str(num)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)
    '''
    return int("".join(sorted(str(num), reverse=True)))
    '''
    
print(Descending_Order(123456))
