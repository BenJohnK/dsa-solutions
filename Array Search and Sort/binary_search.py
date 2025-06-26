#arr = [0, 2, 3, 4, 6]

def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    while (low<=high):
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

lst = list(map(lambda x: int(x), input().split(" ")))
print(binary_search(lst, 6))