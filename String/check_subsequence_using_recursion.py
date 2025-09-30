def check_substring(s1, s2, pointer):
    if s1 == s2 or s2 == "":
        return True
    if s1 == "":
        if pointer == len(s2):
            return True
        else:
            return False
    if s1[0] == s2[pointer]:
        pointer += 1
        if pointer == len(s2):
            return True
    return check_substring(s1[1:], s2, pointer)

print(check_substring("AABCD", "AABCD", 0))