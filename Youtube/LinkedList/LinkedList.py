class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        self.head = new_node

    def print_linked_list(self) :
        if self.head == None :
            print("Empty LinkedList")
            return