class Stack:
    # This is a constructor
    def __init__(self) -> None:
        self.stack = []

    # Push Operation
    def push(self, value):
        self.stack.append(value)

    # Pop Opeartion
    def pop(self):
        self.stack.pop()

    # Printing the result
    def printResult(self):
        return self.stack


s = Stack()
s.push(5)
s.push(7)
s.push(10)
print(s.printResult())
s.pop()
print(s.printResult())
