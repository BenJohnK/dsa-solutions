def lomuto_partition(l, h, arr):
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


def quick_sort(l, h, arr):
    if l>=h:
        return
    p = lomuto_partition(l, h, arr)
    quick_sort(l, p-1, arr)
    quick_sort(p+1, h, arr)

lst = list(map(lambda x: int(x), input().split()))
quick_sort(0, len(lst)-1, lst)

print(lst)