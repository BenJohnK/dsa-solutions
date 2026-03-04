# s = "AABABBA",  k = 1

from collections import defaultdict

def find_longest_repeating_character(s: str, k: int) -> int:
    max_length = 0
    left = 0
    max_frequency = 0
    freq_dict = defaultdict(int)

    for right in range(len(s)):
        freq_dict[s[right]] += 1
        max_frequency = max(max_frequency, freq_dict[s[right]])

        while (right-left+1) - max_frequency > k:
            freq_dict[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right-left+1)


    return max_length

print(find_longest_repeating_character("AABABBA", 1))