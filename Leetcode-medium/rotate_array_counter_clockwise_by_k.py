#Rotate the array in-place

#[1,2,3,4,5,6,7] + 3 -> [4,5,6,7,1,2,3]

#[4,5,6,7,5,6,7]


def rotate(lst, k):
    d = k % len(lst)
    saved_lst = lst[0:d]
    for i in range(d, len(lst)):
        lst[i-d] = lst[i]
    j = 0
    for i in range(len(lst)-d, len(lst)):
        lst[i] = saved_lst[j]
        j += 1
    return lst



lst = [1,2,3,4,5,6,7]
k = 6

print(rotate(lst, k))