def printNonRepeated(arr):
    #Your code here
    counter = {}
    new_arr = []
    for x in arr:
        counter[x] = counter.get(x, 0) + 1
    for k in counter:
        if counter[k] == 1:
            new_arr.append(k)
    return new_arr


print(printNonRepeated([1,2,3,4,4]))