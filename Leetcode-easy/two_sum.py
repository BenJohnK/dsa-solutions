def two_sum(arr, target):
    a = {}
    for i in range(len(arr)):
        a[arr[i]] = i
    for i in range(len(arr)):
        if target - arr[i] in a:
            return [i, a[target - arr[i]]]
    return "No pair"
        

print(two_sum([1, 2, 3], 8))