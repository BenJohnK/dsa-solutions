def check_palindrome(s):
    i = 0                 # constant space. And this extra space for pointers is constant and doesn't depend on the length of the string.
    j = len(s) - 1
    while(i<j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

print(check_palindrome("ABCCBA"))