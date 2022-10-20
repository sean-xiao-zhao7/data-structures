class LinkedList:
    def __init__(self, initial_value):
        self.head = Node(initial_value)
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        output = ""
        current_node = self.head
        while current_node:
            output += f'[Node {current_node.value}] -> '
            current_node = current_node.next
        output += f'\nLength: {self.length}'
        return output

    def append(self, node_value):
        node = Node(node_value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, node_value):
        node = Node(node_value)
        node.next = self.head
        self.head = node
        self.length += 1


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)


if __name__ == "__main__":
    list1 = LinkedList(1)
    list1.append(2)
    list1.append(5)
    list1.prepend(10)
    print(list1)
