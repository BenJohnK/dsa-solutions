from collections import Counter
 
def find_first_non_repeating_character(s: str) -> str | None:
    frequency_table = Counter(s)
    for ch in s:
        if frequency_table[ch] == 1:
            return ch
    return None

print(find_first_non_repeating_character("abbacc"))