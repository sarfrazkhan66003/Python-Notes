def removeDuplicate(input_str):
    set_input = set()
    stack = []
    input_string = input_str

    for char in input_string:
        if char not in set_input:
            stack.append(char)
            set_input.add(char)
    return "".join(stack)


input_str = "aaabcccccccddddffffffewdsjdskhdsjhdjshdshdjshdjshjdhsjdhshdh"
result = removeDuplicate(input_str)
print(result)
