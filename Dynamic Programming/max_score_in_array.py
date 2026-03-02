# Q. Arun is playing an escape game puzzle. Given an array. He can choose a value v and add that value to the score. 
# Then he should delete/not count v - 1 and v + 1 if they exists. For eg: if 11 is taken 10 and 12 should be ignored/deleted. 
# Then pick the next value and repeat 1 and 2 steps till the array is empty. Return the maximum score that can be obtained.

arr = [1,1,1,2,4,5,5,5,6]

from collections import defaultdict


def find_max_score(lst: list) -> int:
    score_dict = defaultdict(int)
    for x in lst:
        score_dict[x] += x
    print(score_dict)
    nums = sorted(score_dict.keys())
    print(nums)
    total_score = score_dict[nums[0]]
    backup_score = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            backup_score = total_score
            total_score += score_dict[nums[i]]
        else:
            take_current_score = backup_score + score_dict[nums[i]]
            if take_current_score > total_score:
                backup_score = total_score
                total_score = take_current_score
            else:
                backup_score = total_score
    return total_score


print(find_max_score(arr))

