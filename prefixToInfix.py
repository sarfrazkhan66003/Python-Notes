stack = []
operator = set(["+", "-", "*", "/", "^"])
expression = "*+abc"

for char in reversed(expression):
    if char not in operator:
        stack.append(char)
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(f"({op1} {char} {op2})")
print(stack.pop())
