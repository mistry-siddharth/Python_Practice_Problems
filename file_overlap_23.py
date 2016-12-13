class File_overlap:

    def __init__(self):
        print('Lets find common numbers from prime nums and happy nums!')
    
    def prime_num(self):
        prime_num = []
        f1op = open('23_prime_nums.txt')
        read1 = f1op.read()
        read1 = read1.split()
        for num1 in read1:
            prime_num.append(int(num1))
        return prime_num

    def happy_num(self):
        happy_num = []
        f2op = open('23_happy_nums.txt')
        read2 = f2op.read()
        read2 = read2.split()
        for num2 in read2:
            happy_num.append(int(num2))
        return happy_num

    def common_num(self, happy_num, prime_num):
        common = []
        for num in happy_num:
            if num in prime_num:
                common.append(num)
        return common
    '''
    if __name__ == '__main__':
        prime_num = prime_num()
        happy_num = happy_num()
        common_num(happy_num, prime_num)
    '''

file_overlap = File_overlap()
prime_num = file_overlap.prime_num()
happy_num = file_overlap.happy_num()
common = file_overlap.common_num(happy_num, prime_num)
print('Common nums are:\n', common)
