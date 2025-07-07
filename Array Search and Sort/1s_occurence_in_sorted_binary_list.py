
def count_1(lst):
    low = 0
    high = len(lst) - 1
    while(low <= high):
        mid = (low + high) // 2
        if lst[mid] == 1:
            if mid == len(lst) - 1 or lst[mid+1] == 0:
                return mid + 1
            low = mid + 1
        else:
            high = mid - 1
    return 0


lst = list(map(lambda x: int(x), input().split(" ")))
print(count_1(lst))
