def check_palindrome(s) -> bool:
    return s == s[::-1]

print(check_palindrome("malayalam"))