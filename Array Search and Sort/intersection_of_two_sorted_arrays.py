#a = [3,5,10,10,19,]
#b = [1,2,2,4,5,5]

def print_intersection(a, b):
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i<m and j<n:
        if i!=0 and a[i] == a[i-1]:
            i+=1
            continue
        if j!=0 and b[j] == b[j-1]:
            j+=1
            continue
        if a[i] == b[j]:
            print(a[i], end=" ")
            i+=1
            j+=1
        elif a[i] > b[j]:
            j+=1
        elif a[i] < b[j]:
            i+=1

a=list(map(lambda x: int(x), input().split()))
b=list(map(lambda x: int(x), input().split()))

print_intersection(a, b)
