#s = "abccd"
import sys

def find_leftmost_non_repeating_character(s: str):
    counter_dict = {}
    for ch in s.lower():
        counter_dict[ch] = counter_dict.get(ch, 0) + 1
    for ch in s.lower():
        if counter_dict[ch] == 1:
            return ch
    return -1

print(find_leftmost_non_repeating_character("ben"))