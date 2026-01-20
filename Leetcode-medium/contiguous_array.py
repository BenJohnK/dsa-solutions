#Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

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
    return max_length

print(findMaxLength([1,0,1,0]))