from stack import Stack


class Queue:
    def __init__(self) -> None:
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def peek(self):
        return self.push_stack.top

    def enqueue(self, new_value):
        self.push_stack.push(new_value)

    def dequeue(self):
        if (self.pop_stack.length == 0):
            self.fill_pop_stack()
        self.pop_stack.pop()

    # helpers

    def fill_pop_stack(self):
        node = self.push_stack.pop()
        while node:
            self.pop_stack.push(node.value)
            node = self.push_stack.pop()

    def __str__(self) -> str:
        return str(self.push_stack) + "\n" + str(self.pop_stack)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print("----")
    queue.dequeue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue)
