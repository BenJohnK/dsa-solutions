def check_string_rotated(s1, s2):
    if len(s1) != len(s2):
        return False
    index_of_first_character_of_s2 = -1
    pointer = 0
    for i in range(len(s1)):
        if s1[i] == s2[pointer]:
            if index_of_first_character_of_s2 == -1:
                index_of_first_character_of_s2 = i
            pointer += 1
        else:
            pointer = 0
            index_of_first_character_of_s2 = -1
            if s1[i] == s2[pointer]:
                pointer += 1
                index_of_first_character_of_s2 = i
    if index_of_first_character_of_s2 == -1:
        return False
    if pointer == len(s2):
        return True
    for i in range(index_of_first_character_of_s2):
        if s1[i] != s2[pointer]:
            return False
        else:
            pointer += 1
    return True

print(check_string_rotated("ABAB", "ABBA"))
