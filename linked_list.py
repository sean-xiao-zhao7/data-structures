from copyreg import constructor


class LinkedList:
    def __init__(self, initial_value):
        self.head = Node(initial_value)
        self.tail = self.head

    def __str__(self) -> str:
        return str(self.head)


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)


if __name__ == "__main__":
    list1 = LinkedList(1)
    print(list1)
