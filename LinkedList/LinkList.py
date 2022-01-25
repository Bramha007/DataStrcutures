from Node import Node


class LinkedList:

    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        if value:
            self.addMultipleNodes(value)

    def addNodeAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length += 1
        # return self.tail

    def addMultipleNodes(self, values):
        for value in values:
            self.addNodeAtEnd(value)

    def addNodeAtBeginning(self, value):
        if self.length == 0:
            self.addNodeAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def addNodeInTheMiddle(self, value, location):
        if location == 0:
            self.addNodeAtBeginning(value)
        elif location >= self.length or location < 0:
            print("Insertion not possible index out of bounds")
            return
        else:
            node = self.head
            for i in range(location-1):
                node = node.next
            new_node = Node(value)
            temp_node = node.next
            new_node.next = temp_node
            node.next = new_node
            self.length += 1

    def printLinkedList(self):
        if self.head is None:
            print(f"[{self.length}] {[]}")
            return
        node = self.head
        l_list = f"[{self.length}] "
        while node:
            l_list += str(node.value) + "-->"
            node = node.next
        print(l_list)
        return

    def deleteTailNode(self):
        if self.head is None:
            print("Cant delete from empty Linked List")
            return
        node = self.head
        while node.next != self.tail:
            node = node.next
        self.tail = node
        node.next = None
        self.length -= 1

    def deleteHeadNode(self):
        if self.head is None:
            print("Cant delete from empty Linked List")
            return
        self.head = self.head.next
        self.length -= 1

    def deleteNode(self, location):
        if self.head is None:
            print("Cant delete from empty Linked List")
            return
        elif location == 0:
            self.deleteHeadNode()
            return
        elif location == self.length-1:
            self.deleteTailNode()
            return
        elif location < 0 or location >= self.length:
            print("Index out of bounds")
            return
        node = self.head
        for i in range(location-1):
            node = node.next
        node_to_delete = node.next
        node.next = node_to_delete.next
        node_to_delete.next = None
        self.length -= 1

    def searchNode(self, value):
        if self.head:
            node = self.head
            for index in range(self.length):
                if value == node.value:
                    print(f"{value} present at index {index}")
                    return index
                node = node.next
            print(f"{value} not present in Linked_List")
            return


linkedList = LinkedList([1, 23, 4, 5])
linkedList.printLinkedList()
linkedList.searchNode(5)
linkedList.addNodeAtBeginning(7)
linkedList.printLinkedList()
linkedList.addNodeInTheMiddle(58, 4)
linkedList.printLinkedList()
linkedList.deleteTailNode()
linkedList.printLinkedList()
linkedList.deleteHeadNode()
linkedList.printLinkedList()
linkedList.deleteNode(2)





