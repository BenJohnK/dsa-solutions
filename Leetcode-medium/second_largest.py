a = [5,1,2,3,4,5]
# a = [1,2,3,5,4]
# a = [5,4,3,2,1]

array_sum = sum(a)
smallest_sum = array_sum - a[0]
largest_element = a[0]
for i in range(1, len(a)):
    if array_sum - a[i] < smallest_sum:
        smallest_sum = array_sum - a[i]
        largest_element = a[i]

if a[0] == largest_element:
    smallest_sum = array_sum - a[1]
    j=2
    second_largest_element = a[1]
else:
    smallest_sum = array_sum - a[0]
    second_largest_element = a[0]
    j=1

for i in range(j, len(a)):
    if a[i] == largest_element:
        continue
    if array_sum - a[i] < smallest_sum:
        smallest_sum = array_sum - a[i]
        second_largest_element = a[i]

print(second_largest_element)