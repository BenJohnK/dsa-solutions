# a = [5, 20, 30, 10]

def insertion_sort(lst, n):
    for i in range(1, n):
        x = lst[i]
        j=i-1
        while j>=0 and x<lst[j]:
            lst[j+1] = lst[j]
            j=j-1
        lst[j+1] = x
    return lst


lst = list(map(lambda x: int(x), input().split()))

print(insertion_sort(lst, len(lst)))