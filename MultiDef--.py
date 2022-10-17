def multi(*nums):
    multi_num = 1
    for numF in nums:
        multi_num *= numF
    
    return multi_num

print(multi(2,3,4,5,6,7,8,9,10,11,12,13,14,15))
