def loop_func():
    a = [1, 2, 3, 4, 5, 1, 3, 6, 8 , 4]
    b = []
    for element in a:
        if element not in b:
            b.append(element)
    return b

def set_func():
    a = [1, 2, 3, 4, 5, 1, 3, 6, 8 , 4]
    return list(set(a))

print(loop_func())
print(set_func())
