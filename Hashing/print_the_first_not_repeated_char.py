def nonRepeatingChar(s):
    #code here
    counter = {}
    count = 0
    for x in s:
        counter[x] = counter.get(x, 0) + 1
    for k in counter:
        if counter[k] == 1:
            return k
    return "$"

print(nonRepeatingChar("geeksforgeeks"))