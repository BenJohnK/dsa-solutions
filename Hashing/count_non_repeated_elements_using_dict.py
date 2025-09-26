def count_non_repeated_elements(arr):
    counter = {}
    count = 0
    for x in arr:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1
    for x in counter:
        if counter[x] == 1:
            count += 1
    return count


print(count_non_repeated_elements([1,2,3,2,2,3,3,4,1,4]))