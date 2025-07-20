# a=[5, 4, 3, 2, 1]

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


lst = list(map(lambda x: int(x), input().split()))

print(bubble_sort(lst))