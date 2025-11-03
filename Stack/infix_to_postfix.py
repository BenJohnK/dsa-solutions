def infix_to_postfix(expr: str):
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    stack = []
    output = ""
    for ch in expr:
        if ch.isalnum():
            output += ch
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while True:
                p = stack.pop()
                if p == "(":
                    break
                output += p
        else:
            if not stack or stack[-1] == "(":
                stack.append(ch)
            elif precedence.get(ch) < precedence.get(stack[-1]):
                i = len(stack) - 1
                while i != -1 and stack[i] != "(":
                    p = stack.pop()
                    output += p
                    i = i -1
                stack.append(ch)
            elif precedence.get(ch) == precedence.get(stack[-1]):
                if ch == "^":
                    stack.append(ch)
                else:
                    p = stack.pop()
                    stack.append(ch)
                    output += p
            else:
                stack.append(ch)
    while stack:
        p = stack.pop()
        output += p
    return output


print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))
# Output: abcd^e-fgh*+^*+i-