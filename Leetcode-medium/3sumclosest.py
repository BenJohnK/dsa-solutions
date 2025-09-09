def threeSumClosest(nums, target):
    lowest_possible_sum = nums[0] + nums[1] + nums[2]
    if target <= lowest_possible_sum:
        return lowest_possible_sum
    highest_possible_sum = nums[-1] + nums[-2] + nums[-3]
    if target >= highest_possible_sum:
        return highest_possible_sum
    closest_sum = lowest_possible_sum
    print(closest_sum)
    difference = target - closest_sum
    for i in range(len(nums)-2):
        print(i)
        j=i+1
        k=len(nums) - 1
        while(j<k):
            print(nums[i] + nums[j] + nums[k])
            if nums[i] + nums[j] + nums[k] == target:
                return target
            if nums[i] + nums[j] + nums[k] < target:
                sum = nums[i] + nums[j] + nums[k]
                calculated_difference = (target - sum)
                if calculated_difference < difference:
                    difference = calculated_difference
                    closest_sum = sum
                j+=1
                
            elif nums[i] + nums [j] + nums[k] > target:
                sum = nums[i] + nums[j] + nums[k]
                calculated_difference = (sum - target)
                if calculated_difference < difference:
                    difference = calculated_difference
                    closest_sum = sum
                k-=1
    return closest_sum


arr = [0,3,97,102,200]
print(sorted(arr))
target = 300

print(threeSumClosest(sorted(arr), target))