def check_anagram(s1, s2, s3):
    if len(s1) != len(s2) or len(s1) != len(s3):
        return "No"
    d = {}
    for x in s1:
        d[x] = d.get(x,0) + 1
    for x in s2:
        if x not in d:
            return "No"
        d[x] -= 1
    for k in d:
        if d[k] != 0:
            return "No"
        
    #At this point if s1 and s2 are anagrams, all the keys in d will have value 0. So use the same dict d to fill again for the string s1.
    for x in s1:
        d[x] += 1
    for x in s3:
        if x not in d:
            return "No"
        d[x] -= 1
    for k in d:
        if d[k] != 0:
            return "No"
    return "Yes"

s1 = "aaa"
s2 = "abc"
s3 = "acc"

print(check_anagram(s1,s2,s3))