# a=[3,5]
# b=[2,8,8,9,10,15]


def print_union(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i<n or j<m:
        if i!=0 and i!=n and a[i] == a[i-1]:
            i+=1
        elif j!=0 and j!=m and b[j] == b[j-1]:
            j+=1
        elif i == n:
            print(b[j], end=" ")
            j += 1
        elif j == m:
            print(a[i], end=" ")
            i += 1
        elif a[i] < b[j]:
            print(a[i], end=" ")
            i+=1
        elif a[i] > b[j]:
            print(b[j], end=" ")
            j+=1
        else:
            print(a[i], end=" ")
            i += 1
            j += 1


a = list(map(lambda x: int(x), input().split()))
b = list(map(lambda x: int(x), input().split()))

print_union(a,b)