#You are allowed to flip at most one element in the array (i.e., change a 0 to 1 or a 1 to 0).
#After performing at most one flip, return the maximum length of a contiguous subarray that contains an equal number of 0s and 1s.

def findMaxLength(nums):
    counter_dict = {0:-1}
    max_length = 0
    total = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            total-=1
        else:
            total+=1
        if total in counter_dict:
            diff = i - counter_dict[total]
            if diff > max_length:
                max_length = diff
        else:
            counter_dict[total] = i
        
        for target in [total+2, total-2]:
            if target in counter_dict:
                max_length = max(max_length, i-counter_dict[target])
    return max_length

print(findMaxLength([1,1,1,0]))