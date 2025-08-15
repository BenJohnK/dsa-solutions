#a = [2,4,1,3,5]


def count_inversions(lst):
    count = 0
    if len(lst) == 1:
        return lst, count
    low = 0
    high = len(lst) - 1
    mid = (low + high) // 2
    a, count_a = count_inversions(lst[0:mid+1])
    b, count_b = count_inversions(lst[mid+1:])
    i = 0
    j = 0
    c = []
    while i<len(a) or j<len(b):
        if i == len(a):
            c.append(b[j])
            j += 1
            continue
        if j == len(b):
            c.append(a[i])
            i += 1
            continue
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
        elif a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            count += len(a) - i
            j += 1
    return c, count_a + count_b + count


lst = list(map(lambda x: int(x), input().split()))
print(count_inversions(lst)[1])
