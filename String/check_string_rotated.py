def check_string_rotated(s1, s2):
    old_string = s1
    if len(s1) != len(s2):
        return False
    for _ in range(len(s1)-1):
        new_str = ""
        for j in range(1, len(old_string)):
            new_str += old_string[j]
        new_str += old_string[0]
        if new_str == s2:
            return True
        old_string = new_str
    return False

print(check_string_rotated("ABAB", "ABBA"))
