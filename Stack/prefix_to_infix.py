def prefix_to_infix(prefix: str):
    stack = []
    prefix_reversed = prefix[::-1]
    for ch in prefix_reversed:
        if ch.isalnum():
            stack.append(ch)
        else:
            p = stack.pop()
            q = stack.pop()
            stack.append(f"({p}{ch}{q})")
    return stack[0]


print(prefix_to_infix("*-A/BC-/AKL"))