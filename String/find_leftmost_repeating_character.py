#s = "abccd"
import sys

def check_leftmost_repeat(s1):
    counter_dict = {}
    res = sys.maxsize
    for i in range(len(s1)):
        if s1[i] not in counter_dict:
            counter_dict[s1[i]] = i
        else:
            res = min(res, counter_dict[s1[i]])
    if res == sys.maxsize:
        return -1
    return res

print(check_leftmost_repeat("abbcd"))