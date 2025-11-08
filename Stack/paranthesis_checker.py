def paranthesis_checker(string: str):
    match_dict = {"}": "{", ")": "(", "]": "["}
    open_set = {"(", "{", "["}
    stack = []
    for ch in string:
        if ch in open_set:
            stack.append(ch)
        elif stack and match_dict[ch] == stack[-1]:
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True

print(paranthesis_checker("([{]})"))