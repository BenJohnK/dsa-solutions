def remove_duplicates(lst):
    # Convert each sublist to a tuple to make it hashable, then add to a set
    unique_tuples = {tuple(sublist) for sublist in lst}
    
    # Convert back to list of lists
    unique_lists = [list(t) for t in unique_tuples]
    
    return unique_lists

def threeSum(nums):
    lst = []
    for i in range(len(nums)):
        number = nums[i]
        if number < 0:
            number = 0 - (number)
        elif number > 0:
            number = 0 - (number)
        j=0
        k=len(nums) - 1
        while(j<k):
            if i == j:
                j+=1
                continue
            if i == k:
                k-=1
                continue
            if nums[j] + nums[k] == number:
                lst.append(sorted([nums[i], nums[j], nums[k]]))
                j+=1
                k-=1
            elif nums[j] + nums[k] < number:
                j+=1
                continue
            else:
                k-=1
                continue
        
    return remove_duplicates(lst)


arr = list(map(lambda x: int(x), input().split()))

print(threeSum(sorted(arr)))