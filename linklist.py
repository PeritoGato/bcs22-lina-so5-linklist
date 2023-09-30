class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head or self.head.value < value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value > value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next


elements = [6, 4, 3, 2, 1]

linked_list = LinkedList()
for element in elements:
    linked_list.insert(element)

linked_list.display()