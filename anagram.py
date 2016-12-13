def isAnagram(s, t):
    '''
    if s == '' and t == '':
        return True

    if len(s) != len(t):
        return False

    s_dict = dict()
    t_dict = dict()
    
    for x in s:
        s_dict[x] = s_dict.get(x, 0) + 1

    for x in t:
        t_dict[x] = t_dict.get(x, 0) + 1

    for (ks, vs), (kt, vt) in zip(s_dict.items(), t_dict.items()):
        if ks == kt and vs == vt:
            return True
        else:
            return False
    '''
    s = sorted(s)
    print(s)
    t = sorted(t)
    print(t)

    if s == t:
        return True
    else:
        return False

print(isAnagram("anagram", "nagaram"))
