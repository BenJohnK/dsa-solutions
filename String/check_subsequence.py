#s1 = "AABCD"
#s2 = "BC"

def check_subsequence(s1, s2):
    if s1 == s2 or s2 == "":
        return True
    pointer = 0
    for i in range(len(s1)):
        if s1[i] == s2[pointer]:
            pointer += 1
            if pointer == len(s2):
                return True
    if pointer != len(s2):
        return False
    return True

print(check_subsequence("AABCD", "AABC"))