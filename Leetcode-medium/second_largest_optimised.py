# a = [1,2,3,4,5]
# a = [1,2,3,5,4]
# a = [5,4,3,2,1]
# a = [4,5,3,2,1]
# a = [5,3,4,4,3,2,1]
# a=[4,5,62,62]
a = [20,20,18]

largest = a[0]
second_largest = a[0]

for i in range(len(a)):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
    else:
        if a[i] > second_largest and a[i] != largest:
            second_largest = a[i]
        else:
            if largest == second_largest:
                second_largest = a[i]

print(largest, second_largest)