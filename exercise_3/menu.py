"""
Module for linked list menu operations.
"""

from linked_list import LinkedList

class Menu:
    def __init__(self):
        self.linked_list = LinkedList()

    def valid_choice(self, choice):  # Validate user choice
        return choice in ['1', '2', '3', '4', '5', '6']

    """Check the linked_list.py file for the LinkedList class implementation."""
    def insert_node(self):  # Insert a node
        data = input("Please enter a data: ")
        self.linked_list.insert(data)

    def delete_node(self):  # Delete a node
        key = input("Please enter data to be deleted: ")
        self.linked_list.delete(key)

    def search_node(self):  # Search for a node
        key = input("Please enter data to be searched: ")
        self.linked_list.search(key)

    def display_list(self):  # Display the linked list
        pass

    def reverse_list(self):  # Reverse the linked list
        pass

    def exit_program(self): # Exits the program
        print("Exiting program...")
        exit()