def dirReduc(arr):
    prev = 0
    new_list = []
    
    for x in arr:
        if x == 'NORTH' and prev != 'NORTH' and prev != 'SOUTH':
            new_list.append(x)
            prev = x
        elif x == 'SOUTH' and prev != 'NORTH' and prev != 'SOUTH':
            new_list.append(x)
            prev = x
        elif x == 'EAST' and prev != 'EAST' and prev != 'WEST':
            new_list.append(x)
            prev = x
        elif x == 'WEST' and prev != 'EAST' and prev != 'WEST':
            new_list.append(x)
            prev = x
        
    return new_list

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
