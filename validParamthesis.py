stack = []
open_braces = ["(", "{"]
closed_braces = [")", "}"]
string_input = "{()}"

for i in string_input:
    if i in open_braces:
        stack.append(i)
    elif i not in open_braces and i in closed_braces and len(stack) != 0:
        index = closed_braces.index(i)
        if open_braces[index] == stack[len(stack) - 1]:
            stack.pop()

if len(stack) == 0:
    print("Valid")
else:
    print("Not Valid")
