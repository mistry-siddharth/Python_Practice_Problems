a = [5, 10, 15, 20, 25, 1, 3]

def get_reverse():
    b = []
    b = [i for i in a if i == a[0] or i == a[-1]]
    return b

print(get_reverse())
