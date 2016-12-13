with open('read_21_2.txt', 'r') as myfile:
    category_dict = dict() # dictionary to hold counts of category occurrences
    line = myfile.readline() # read a line from the file
    while line: # until a line can be read, grab the category
        category = line.split('/')[2] # category is the 3rd item in split string
        category_dict[category] = category_dict.get(category, 0) + 1 # if the category was already looked at, add one.
                                                                                 # otherwise, create an entry with 0, and add one.
        line = myfile.readline()
    print(category_dict)
