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
            self.length += 1

    def pop(self):
        if (self.length > 0):
            temp = self.top
            self.top = self.top.next
            self.length -= 1
            return temp

    def __str__(self):
        if (self.length <= 0):
            return 'Stack empty'
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
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.push(5)
    stack.pop()
    print(stack)
