class Node:
    def __init__(self, value, next=None, previous=None) -> None:
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self) -> str:
        return f'[Node {self.value}]'
