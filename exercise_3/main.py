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
    menu = Menu()

    # Match each menu choice with its action
    actions = {
        '1': menu.insert_node,
        '2': menu.delete_node,
        '3': menu.search_node,
        '4': menu.display_list,
        '5': menu.reverse_list,
        '6': menu.exit_program
    }

    display_menu()

if __name__ == "__main__":
    main()