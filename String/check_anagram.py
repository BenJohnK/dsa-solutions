def areAnagrams(s1, s2):
    # code here
    if (len(s1) != len(s2)):
        return False
    counter_dict = {}
    for x in s1:
        counter_dict[x] = counter_dict.get(x, 0) + 1
    for x in s2:
        if x not in counter_dict:
            return False
        counter_dict[x] -= 1
    for x in counter_dict:
        if counter_dict[x] != 0:
            return False
    return True

print(areAnagrams("geeks", "kseeg"))