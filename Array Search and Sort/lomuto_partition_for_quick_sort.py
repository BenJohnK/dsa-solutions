# a=[10,80,30,90,40,50,70]

# considering the last element as pivot.

def lomuto_partition(l, h, arr):
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]


lst = list(map(lambda x: int(x), input().split()))
lomuto_partition(0, len(lst)-1, lst)

print(lst)