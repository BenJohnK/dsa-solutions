'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false
'''


def isValid(s: str) -> bool:
    stack = []
    symbol_dict = {"}": "{", ")": "(", "]": "["}
    for ch in s:
        if ch not in symbol_dict:
            stack.append(ch)
        else:
            if not stack:
                return False
            item = stack.pop()
            if symbol_dict[ch] != item:
                return False
    return True if not stack else False

print(isValid("()[]{}"))