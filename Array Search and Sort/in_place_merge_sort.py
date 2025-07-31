#a = [8,6,4,2,10,5,3,1]

from merge_sorted_sub_arrays import sort_sub_array

def merge_sort(lst, low, high):
    if low == high:
        return
    mid = (low+high) // 2
    merge_sort(lst, low, mid)
    merge_sort(lst, mid+1, high)
    sort_sub_array(lst, low, mid, high)


lst = list(map(lambda x: int(x), input().split()))
low = 0
high = len(lst) - 1
merge_sort(lst, low, high)

print(lst)