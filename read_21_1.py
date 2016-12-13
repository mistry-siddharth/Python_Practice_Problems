def read_file(fname):
    fopen = open(fname, 'r')
    readtxt = fopen.read()
    words = readtxt.split()

    count_dict = {}

    for wrd in words:
        if wrd in count_dict:
            count_dict[wrd] += 1
        else:
            count_dict[wrd] = 1

    return count_dict

if __name__ == '__main__':
    fname = input('Enter a file name to read: ')
    file_op = read_file(fname)
    print(file_op)
