def find_outlier(integers):
    n = 0
    odd = []
    even = []
    
    for x in integers:
        if x%2 != 0:
            odd.append(x)
        elif x%2 == 0:
            even.append(x)
    print(odd)
    print(len(odd))
    print(even)
    print(len(even))
    
    if len(odd) == 1:
        n = odd[0]
    elif len(even) == 1:
        n = even[0]
            
    return n
