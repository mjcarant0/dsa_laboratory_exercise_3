"""
Main program to run the linked list menu.
"""

from menu import Menu

def display_menu():  # Display menu options
    options = ["1. Insert Node", "2. Delete Node", "3. Search Node", "4. Display List", "5. Reverse List", "6. Exit"]

    print("\n====== LINKED LIST MENU ======")
    print("\n".join(options))
    print("==============================\n")

def main(): # Main function to run the menu loop
    """Create validation checker loop for menu choices and call appropriate methods."""
    display_menu()

if __name__ == "__main__":
    main()