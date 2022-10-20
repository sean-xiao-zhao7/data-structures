from copyreg import constructor


class LinkedList:
    def __init__(self, node_value):
        self.head = node_value
        self.next = None

    def __str__(self) -> str:
        return str(self.head)


if __name__ == "__main__":
    list1 = LinkedList(1)
    print(list1)
