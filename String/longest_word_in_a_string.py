# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def longest_word(string):
    max_length = 0
    current_length = 0
    current_word = ""
    longest_word = ""

    for ch in string:
        if ch != " ":
            current_word += ch
            current_length += 1 
        else:
            if current_length > max_length:
                max_length = current_length
                longest_word = current_word
            current_word = ""
            current_length = 0
    if current_length > max_length:
        longest_word = current_word
    return longest_word
        
    

string = "ben is a programmer"
print(longest_word(string))