class DoublyLinkedList:
    def __init__(self, initial_value):
        self.head = Node(initial_value)
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        output = ""
        current_node = self.head
        while current_node:
            output += f'[Node {current_node.value}] <-> '
            current_node = current_node.next
        output += f'\nLength: {self.length}'
        return output

    def append(self, node_value):
        node = Node(node_value)
        self.tail.next = node
        node.previous = self.tail
        self.tail = node
        self.length += 1

    def prepend(self, node_value):
        node = Node(node_value)
        node.next = self.head
        self.head.previous = node
        self.head = node
        self.length += 1

    def insert(self, node_value, index):
        if index == 0:
            self.prepend(node_value)
        elif index >= self.length:
            self.append(node_value)
        else:
            (current_node, previous_node) = self.traverse(index)
            new_node = Node(node_value)
            # previous
            previous_node.next = new_node
            new_node.previous = previous_node
            # next
            new_node.next = current_node
            current_node.previous = new_node
            self.length += 1

    def remove(self, index):
        if (self.length == 1):
            self.head = None
            self.length = 0
        elif (index == 0):
            self.head.next.previous = None
            self.head = self.head.next
            self.length -= 1
        else:
            (current_node, previous_node) = self.traverse(index)
            previous_node.next = current_node.next
            current_node.next.previous = previous_node
            self.length -= 1

    # helper methods
    def traverse(self, index):
        """Return current and previous nodes at index"""
        current_index = 0
        current_node = self.head
        previous_node = None
        while current_node.next:
            if index == current_index:
                return (current_node, previous_node)
            previous_node = current_node
            current_node = current_node.next
            current_index += 1
        return (current_node, previous_node)


class Node:
    def __init__(self, value, next=None, previous=None) -> None:
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self) -> str:
        return f'[Node {self.value}]'


if __name__ == "__main__":
    list1 = DoublyLinkedList(1)
    list1.append(2)
    list1.append(5)
    list1.prepend(10)
    list1.insert(12, 1)
    # list1.remove(0)
    print(list1)
