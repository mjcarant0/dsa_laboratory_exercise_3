'''
Program that demonstrates insertion at the beginning of a singly linked list. 
'''

from basic_operations import LinkedList, Node

class InsertionVariations(LinkedList):
    def insert_beginning(self, data):  # Implement a function for insertion of new nodes at the beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Test for implementation
ll = InsertionVariations()
ll.insert_end(11)
ll.insert_end(88)

print("Linked List after inserting at the end:")
ll.display()

# Insert a node at the beginning and display the updated list
print("\nInsert at the beginning:")
ll.insert_beginning(77)
ll.display()
