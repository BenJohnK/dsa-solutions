#s = "abccd"
import sys

def find_leftmost_non_repeating_character(s: str):
    counter_dict = {}
    for x in s.lower():
        counter_dict[x] = counter_dict.get(x, 0) + 1
    for k in counter_dict:
        if counter_dict[k] == 1:
            return k
    return -1

print(find_leftmost_non_repeating_character("teeter"))