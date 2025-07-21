# a = [5,4,3,2,1]

def selection_sort(lst, n):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst


lst = list(map(lambda x: int(x), input().split()))
print(selection_sort(lst, len(lst)))

