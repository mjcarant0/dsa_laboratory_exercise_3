<div align="center">

# Exercise #3

</div>

## Challenge Task

### Overview

This program implements a menu-driven system for managing a linked list. It allows users to perform operations such as inserting, deleting, searching, displaying, and reversing the linked list.

---

### How the Code Works

#### 1. **Linked List**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```
- **Purpose:**  
  This defines the `Node` class, which represents a single element in the linked list.
- **How:**  
  - The `Node` class has two attributes:
    - `data`: Stores the value of the node.
    - `next`: Points to the next node in the list (or `None` if it’s the last node).
  - The `__init__` method initializes these attributes when a new node is created.

---

```python
class LinkedList:
    def __init__(self):
        self.head = None
```
- **Purpose:**  
  This initializes the `LinkedList` class, which manages the linked list.
- **How:**  
  - The `LinkedList` class has one attribute:
    - `head`: Points to the first node in the list (or `None` if the list is empty).
  - The `__init__` method sets `head` to `None` when a new linked list is created.

---

```python
def insert(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    print(f"Node with data '{data}' inserted.")
```
- **Purpose:**  
  Adds a new node to the beginning of the linked list.
- **How:**  
  - A new `Node` object is created with the given `data`.
  - The `next` pointer of the new node is set to the current `head` of the list.
  - The `head` of the list is updated to point to the new node.
  - A message is printed to confirm the insertion.

---

```python
def delete(self, key):
    temp = self.head
    if temp is not None and temp.data == key:
        self.head = temp.next
        temp = None
        print(f"Node with data '{key}' deleted.")
        return
    prev = None
    while temp is not None and temp.data != key:
        prev = temp
        temp = temp.next
    if temp is None:
        print(f"Node with data '{key}' not found.")
        return
    prev.next = temp.next
    temp = None
    print(f"Node with data '{key}' deleted.")
```
- **Purpose:**  
  Deletes the first node in the linked list that contains the specified `key`.
- **How:**  
  - If the `head` node contains the `key`, it is removed, and the `head` is updated.
  - Otherwise, the method traverses the list to find the node with the `key`.
  - If found, the node is unlinked from the list by updating the `next` pointer of the previous node.
  - If not found, a message is printed.

---

```python
def search(self, key):
    temp = self.head
    while temp:
        if temp.data == key:
            print(f"Node with data '{key}' found.")
            return True
        temp = temp.next
    print(f"Node with data '{key}' not found.")
    return False
```
- **Purpose:**  
  Searches for a node with the specified `key` in the linked list.
- **How:**  
  - The method starts at the `head` and traverses the list.
  - If a node with the `key` is found, a success message is printed, and `True` is returned.
  - If the end of the list is reached without finding the `key`, a failure message is printed, and `False` is returned.

---

```python
def display(self):
    if self.head is None:
        print("The list is empty.")
        return
    temp = self.head
    print("Linked List:", end=" ")
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
```
- **Purpose:**  
  Displays all the nodes in the linked list.
- **How:**  
  - If the list is empty (`head` is `None`), a message is printed.
  - Otherwise, the method starts at the `head` and traverses the list, printing the `data` of each node followed by an arrow (`->`).
  - The traversal ends with `None` to indicate the end of the list.

---

```python
def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
    print("Linked list reversed.")
```
- **Purpose:**  
  Reverses the order of the nodes in the linked list.
- **How:**  
  - The method uses three pointers: `prev`, `current`, and `next_node`.
  - It iterates through the list, reversing the `next` pointer of each node to point to the previous node.
  - At the end of the iteration, the `head` is updated to the last node (now the first node in the reversed list).
  - A message is printed to confirm the reversal.

---

#### 2. **Menu**
```python
from linked_list import LinkedList
```
- **Purpose:**
  Imports the `LinkedList` class from the `linked_list` module so the menu can access and control linked list operations.
- **How:**  
  - Uses Python’s `import` statement to access code from another file.
  - Only imports the `LinkedList` class (not the entire module).
  - Enables the menu to create and manipulate a linked list through class methods.

---

```python
class Menu:
    def __init__(self):
        self.linked_list = LinkedList()
```
- **Purpose:**
  Initializes the `Menu` class and creates an instance of the linked list to perform operations on.
- **How:**  
  - Defines the constructor method `__init__`.
  - Instantiates `LinkedList` and stores it in `self.linked_list`.
  - Ensures all menu actions operate on the same linked list instance.

---

```python
def valid_choice(self, choice):
    return choice in ['1', '2', '3', '4', '5', '6']
```
- **Purpose:**
  Checks if the user’s input corresponds to a valid menu option.
- **How:**  
  - Accepts the user’s input `choice` as a parameter.
  - Compares it against a predefined list of valid options.
  - Returns `True` if the input matches one of the options, otherwise `False`.

---

```python
def insert_node(self):
    data = input("Please enter a data: ")
    self.linked_list.insert(data)
```
- **Purpose:**
  Allows the user to insert a new node with the specified data into the linked list.
- **How:**  
  - Prompts the user to enter a value for the new node.
  - Passes the input to the `insert` method of the linked list.
  - The linked list then creates and adds the new node.

---

```python
def delete_node(self):
    key = input("Please enter data to be deleted: ")
    self.linked_list.delete(key)
```
- **Purpose:**
  Removes a node containing the specified data from the linked list.
- **How:**  
  - Prompts the user to input the value they want to remove.
  - Sends this value to the linked list’s `delete` method.
  - The linked list searches for and deletes the node with the matching data.

---

```python
def search_node(self):
    key = input("Please enter data to be searched: ")
    self.linked_list.search(key)
```
- **Purpose:**
  Searches for a node containing the specified data in the linked list.
- **How:**  
  - Prompts the user to input the data they want to find.
  - Passes the value to the linked list’s `search` method.
  - Displays whether the node was found or not based on the search result.

---

```python
def display_list(self):
    self.linked_list.display()
```
- **Purpose:**
  Displays all nodes currently stored in the linked list.
- **How:**  
  - Calls the linked list’s `display` method directly.
  - The linked list traverses its nodes from head to tail.
  - Prints each node’s data in order.

---

```python
def reverse_list(self):
    self.linked_list.reverse()
```
- **Purpose:**
  Reverses the order of the nodes in the linked list.
- **How:**  
  - Invokes the linked list’s `reverse` method.
  - The method rearranges the links between nodes to point in the opposite direction.
  - Updates the head pointer to reflect the reversed list.

---

```python
def exit_program(self):
    print("Exiting program...")
    exit()
```
- **Purpose:**
  Ends the program when the user chooses the exit option.
- **How:**  
  - Prints a message to indicate the program is closing.
  - Calls Python’s built-in `exit()` function to terminate execution.
  - Ensures a clean and immediate program shutdown.

---

#### 3. **Main**
```python
from menu import Menu
```
- **Purpose:**
  Imports the `Menu` class from the `menu` module so its methods can be used to manage linked list operations.
- **How:**  
  - Uses Python’s `import` statement to access external code from the `menu.py` file.
  - Brings only the `Menu` class (not the entire module) into the current script’s namespace.
  - Allows direct creation of a Menu object without needing to prefix it with `menu.`.

---

```python
def display_menu():
  options = ["1. Insert Node", "2. Delete Node", "3. Search Node", "4. Display List", "5. Reverse List", "6. Exit"]

  print("\n====== LINKED LIST MENU ======")
  print("\n".join(options))
  print("==============================\n")
```
- **Purpose:**
  Displays the menu options for performing operations on the linked list.
- **How:**  
  - A list of string options is created representing each menu action.
  - `"\n".join(options)` is used to print all options neatly in a column format.
  - Decorative lines are printed above and below to make the menu more readable.

---

```python
def main():
    menu = Menu()
    actions = {
        '1': menu.insert_node,
        '2': menu.delete_node,
        '3': menu.search_node,
        '4': menu.display_list,
        '5': menu.reverse_list,
        '6': menu.exit_program
    }
```
- **Purpose:**
  Initializes the menu system and maps user choices to their corresponding linked list operations.
- **How:**  
  - Creates an instance of the `Menu` class to access linked list functions.
  - Uses a dictionary (`actions`) to associate menu numbers with their respective methods.
  - Simplifies method calling by mapping user input directly to the right function.

---

```python
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    if not menu.valid_choice(choice):
        print("Invalid choice. Please try again.")
        continue
    actions[choice]()
```
- **Purpose:**
  Continuously displays the menu, handles user input, and executes the corresponding linked list operation.
- **How:**  
  - Calls `display_menu()` to show the menu options on every loop iteration.
  - Accepts user input and validates it using `menu.valid_choice()`.
  - If valid, retrieves and calls the corresponding method from the `actions` dictionary.
  - If invalid, displays an error message and prompts again.

---

```python
if __name__ == "__main__":
    main()
```
- **Purpose:**
  Ensures that the program runs the `main()` function only when the file is executed directly.
- **How:**  
  - Checks if the script is the entry point (`__name__ == "__main__"`).
  - Calls the `main()` function to start the linked list menu system.
  - Prevents `main()` from running automatically if the script is imported as a module.

---

### Summary

- **Linked List**: Contains the core logic for linked list operations, including `insert`, `delete`, `search`, `display`, and `reverse`.
- **Menu**: Provides a user interface to interact with the linked list through options like `Insert Node`, `Delete Node`, `Search Node`, `Display List`, and `Reverse List`.
- **Main:** Acts as the `entry point`, displaying the menu and handling user input to call the appropriate linked list operations.