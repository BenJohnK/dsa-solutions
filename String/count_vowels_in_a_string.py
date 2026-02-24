# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def count_vowels(string):
    vowel_set = {"a", "e", "i", "o", "u"}
    vowel_count = 0
    for ch in string:
        if ch in vowel_set:
            vowel_count += 1
    return vowel_count

string = "ben"
print(count_vowels(string))