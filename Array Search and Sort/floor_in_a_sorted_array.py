# Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x. 
# This element is called the floor of x. If such an element does not exist, return -1.

# Note: In case of multiple occurrences of ceil of x, return the index of the last occurrence

def floor_in_array(lst, x):
    low = 0
    high = len(lst) - 1
    while(low<=high):
        mid = (low + high) // 2
        if lst[mid] > x:
            high = mid - 1
        else:
            if mid == len(lst) - 1 or lst[mid + 1] > x:
                return mid
            low = mid + 1
    return -1


lst = list(map(lambda x: int(x), input().split()))
x = int(input())
print(floor_in_array(lst, x))