# a=[2,4,6,8] b=[1,3,5,10]

def merge_two_sorted_arrays(a,b):
    m, n = len(a), len(b)
    c = []
    i = 0
    j = 0
    while i<m or j<n:
        if i == m:
            c.append(b[j])
            j+=1
            continue
        if j == n:
            c.append(a[i])
            i+=1
            continue
        if a[i] <= b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    return c



# a = list(map(lambda x: int(x), input().split()))
# b = list(map(lambda x: int(x), input().split()))

# print(merge_two_sorted_arrays(a,b))