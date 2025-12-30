class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("stack is empty")
        popped_value = self.head.data
        self.head = self.head.next
        return popped_value

    def print(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next


if __name__ == "__main__":
    s = Stack()
    s.push(4)
    s.push(8)
    s.push(9)
    s.pop()
    s.pop()
    s.print()
