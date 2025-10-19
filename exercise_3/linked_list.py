"""
Module for linked list data structure implementation.
"""

# Linked List Node Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Implementation
class LinkedList:
    def __init__(self):  # Initialize the linked list
        self.head = None

    def insert(self, data):  # Insert a new node at the beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Node with data '{data}' inserted.")

    def delete(self, key):  # Delete a node by value
        temp = self.head
        if temp is not None and temp.data == key:  # If head node holds the key
            self.head = temp.next
            temp = None
            print(f"Node with data '{key}' deleted.")
            return
        prev = None
        while temp is not None and temp.data != key:  # Search for the key
            prev = temp
            temp = temp.next
        if temp is None:  # Key not found
            print(f"Node with data '{key}' not found.")
            return
        prev.next = temp.next  # Unlink the node
        temp = None
        print(f"Node with data '{key}' deleted.")

    def search(self, key):  # Search for a node by value
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Node with data '{key}' found.")
                return True
            temp = temp.next
        print(f"Node with data '{key}' not found.")
        return False

    def display(self):  # Display the linked list
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):  # Reverse the linked list
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Linked list reversed.")