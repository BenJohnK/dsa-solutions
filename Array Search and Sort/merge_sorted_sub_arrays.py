#a=[2,4,6,8,1,3,5,10]

def sort_sub_array(lst, low, mid, high):
    c = []
    i = low
    j = mid + 1
    while i<mid+1 or j< high+1:
        if i == mid+1:
            c.append(lst[j])
            j+=1
            continue
        if j == high+1:
            c.append(lst[i])
            i+=1
            continue
        if lst[i] <= lst[j]:
            c.append(lst[i])
            i+=1
        else:
            c.append(lst[j])
            j+=1
    t=0
    for i in range(low, high+1):
        lst[i] = c[t]
        t+=1

# lst = list(map(lambda x: int(x), input().split()))
# low = 0
# high = len(lst) - 1
# mid = (low+high) // 2

# sort_sub_array(lst, low, mid, high)

# print(lst)
