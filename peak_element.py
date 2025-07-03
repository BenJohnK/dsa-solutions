#a = [1, 2, 4, 3, 10, 5, 8]

def peak_element(lst):
    low = 0
    high = len(lst) - 1
    last_index = high
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return 0
        else:
            return 1
    while(low <= high):
        mid = (low + high) // 2
        if mid == 0 or mid == last_index:
            return mid
        if lst[mid] > lst[mid-1] and lst[mid] > lst[mid+1]:
            return mid
        if lst[mid] < lst[mid+1]:
            low = mid + 1
        else:
            high = mid - 1



lst = list(map(lambda x: int(x), input().split(" ")))
print(peak_element(lst))
