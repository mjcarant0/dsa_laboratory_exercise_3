'''
Program that demonstrates insertion at the beginning and a new node after a specific node of a singly linked list. 
'''

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linkedlist class 
class LinkedList:
    def __init__(self):
        self.head = None

    # Display all nodes 
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Insert a node at the end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert a node at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node after a specific node.
    def insert_after(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

# Test implementation
ll = LinkedList() 

# Insert nodes at the end
ll.insert_end(11)
ll.insert_end(88)

print("Linked List after inserting at the end:")
ll.display()

# Insert a node at the beginning and display the updated list
print("\nInsert at the beginning:")
ll.insert_beginning(77)
ll.display()
