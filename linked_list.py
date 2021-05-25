
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def to_dict(self):
        the_dict = {}
        node = self.head
        while node:
            the_dict[str(node.data.date)] = node.data.id
            node = node.next_node
        return the_dict

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
