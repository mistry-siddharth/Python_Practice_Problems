def removeDuplicates(nums):
    '''
    nums.sort()
    i = len(nums) - 1
    while i > 0:  
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        i -= 1
    return nums
    '''
    
    temp = 0
    for x in nums:
        if x == temp:
            nums.pop(x)
    print(nums)
    return nums

print(removeDuplicates([1,1,2,3,4]))
