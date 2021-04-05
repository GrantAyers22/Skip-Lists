# A linked list node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
# Class to create a Doubly Linked List
class DLL:
 
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
 
    # Given a reference to the head of DLL and integer,
    # appends a new node at the end
    def append(self, new_data):
 
        # 1. Allocates node
        # 2. Put in the data
        new_node = Node(new_data)
 
        # 3. This new node is going to be the last node,
        # so make next of it as None
        # (It already is initialized as None)
 
        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
 
        # 6. Change the next of last node
        last.next = new_node
 
        # 7. Make last node as previous of new node
        new_node.prev = last
 
        return
 
    # This function prints contents of linked list
    # starting from the given node
    def printList(self, node):
 
        print("*****Doubly-Linked-List*****")
        while node:
            print("%d" % (node.data), end=" ")
            last = node
            node = node.next
        print()
    
    def delete(self, x):
        node = self.head
        while (node.data != x):
            if node.next == None:
                print("Could not delete node with value " + str(x))
                return
            node = node.next

        # Setting up the list to skip the deleted node from both directions
        (node.prev).next = node.next
        (node.next).prev = node.prev
        del node

class DoublyLinkedList():
    def __init__(self):
        self.DataStructure = DLL()
    
    def insertElement(self, x):
        self.DataStructure.append(x)
    
    def searchElement(self, x):
        node = self.DataStructure.head
        while (node.data != x):
            node = node.next
            if node.next == None:
                return
    
    def deleteElement(self, x):
        node = self.searchElement(x)
        self.DataStructure.delete(node)
    
    def accessElement(self, index):
        counter = 0
        temp_head = self.DataStructure.head
        while (counter <= index):
            temp_head = temp_head.next
            if temp_head == None:
                return
            counter += 1
            
    def displayList(self):
        self.DataStructure.printList(self.DataStructure.head)
    

