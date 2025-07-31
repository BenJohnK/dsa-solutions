# lst=[8, 6, 4, 2, 10, 5, 3, 1]

from merge_two_sorted_arrays import merge_two_sorted_arrays

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    low = 0
    high = len(lst) - 1
    mid = (low+high) // 2
    a = merge_sort(lst[0:mid+1])
    b = merge_sort(lst[mid+1:])
    return merge_two_sorted_arrays(a, b)


lst = list(map(lambda x: int(x), input().split()))
print(merge_sort(lst))