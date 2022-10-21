from node import Node


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, new_value):
        new_node = Node(new_value)
        if (not self.top):
            self.top = new_node
            self.bottom = new_node
            self.length = 1
        else:
            top_node = self.top
            new_node.next = top_node
            self.top = new_node

    def pop(self):
        pass

    def __str__(self):
        output = ""
        current_node = self.top
        while current_node:
            output += str(current_node) + " -> "
            current_node = current_node.next
        return output


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
