<div align="center">

# Exercise #3

</div>

---

## Challenge Task

### Overview

To be Added

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
```[Code] (To be added)
```
- **Purpose:** To be added
- **How:**  
  - To be Added
  - To be Added
  - To be Added

---

#### 2. **Main**
```[Code] (To be added)
```
- **Purpose:** To be added
- **How:**  
  - To be Added
  - To be Added
  - To be Added

---

### Summary

- To be Added
- To be Added
- To be Added