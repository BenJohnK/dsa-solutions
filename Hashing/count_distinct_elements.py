#a = [10,10,10]

def count_distinct_elements(arr):
    if not arr:
        return 0
    count = 1
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] == arr[j]:
                break
        else:
            count += 1
    return count

print(count_distinct_elements([1,1,2,2,3,3]))