

def recursive_binary_search(arr, x, low, high):
    if (low > high):
        return False
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return recursive_binary_search(arr, x, mid+1, high)
    else:
        return recursive_binary_search(arr, x, low, mid-1)
    

arr = list(map(lambda x: int(x), input().split(" ")))
print(recursive_binary_search(arr, 1, 0, len(arr)-1))