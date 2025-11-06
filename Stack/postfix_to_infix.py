def postfix_to_infix(postfix: str):
    stack = []
    for ch in postfix:
        if ch.isalnum():
            stack.append(ch)
        else:
            p = stack.pop()
            q = stack.pop()
            stack.append(f"({q}{ch}{p})")
    return stack[0]

print(postfix_to_infix("abc+*"))