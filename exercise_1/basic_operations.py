"""
Program to demonstrate basic operations on a singly linked list: insertion, deletion, searching, and displaying the list.
"""

# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self): # Display the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_end(self, data): # Insert a new node at the end
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key): # Delete a node by value
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Value not found.")
            return
        prev.next = current.next
        current = None

    def search(self, key): # Search for a node by value
        current = self.head
        while current:
            if current.data == key:
                print(f"{key} found in the list.")
                return True
            current = current.next
        print(f"{key} not found in the list.")
        return False
            
# Execution
ll = LinkedList()

print("=" * 40)
print("Linked List after insertion:")
print("=" * 40)
ll.insert_end(5)
ll.insert_end(15)
ll.insert_end(25)
ll.insert_end(35)
ll.display()

print("=" * 40)
print("Delete node with value 15")
print("=" * 40)
ll.delete_node(15)
ll.display()

print("=" * 40)
print("Search for value 25")
print("=" * 40)
ll.search(25)

print("=" * 40)
print("Final linked list:")
print("=" * 40)
ll.display()
