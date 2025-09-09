def is_valid_paranthesis(string):
    lst = []
    i = -1
    for x in string:
        if x == "[" or x == "{" or x == "(":
            lst.append(x)
            i+=1
        if x == "]" or x == "}" or x == ")":
            if not lst:
                return False
            if x == "]":
                if lst[i] != "[":
                    return False
            elif x == "}":
                if lst[i] != "{":
                    return False
            elif x == ")":
                if lst[i] != "(":
                    return False
            lst.pop()
            i = i-1
    if lst:
        return False
    return True

print(is_valid_paranthesis("{{({})}}"))