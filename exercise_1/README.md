<div align="center">

# Exercise #1

</div>

---

## Basic Operations

### Overview

A linked list is a linear data structure where each element (called a node) contains data and a reference (or “link”) to the next node in the sequence.
Unlike arrays, linked lists use dynamic memory, meaning they can grow or shrink as needed without wasting space.

---

### How the Code Works

#### 1. **Linked List**
```python 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```
- **Purpose:** To create a single node that holds data and a reference to the next node.
- **How:**  
  - The "self.data" stores the value.
  - The "self.next" starts as None because the new node doesn’t point to anything yet.
  - When the nodes are linked together, next connects to another node.

---

```python 
class LinkedList:
    def __init__(self):
        self.head = None
```
- **Purpose:** To manage the entire linked list.
- **How:**  
  - The "self.head" is the first node in the list.
  - It’s set to None at first since the list is empty.
  - All operations (insert, delete, search) start from head.

---

```python
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```
- **Purpose:** To print all nodes in the list, showing how they are linked.
- **How:**
  - Starts from the head and moves through each node.
  - Prints the data followed by an arrow (->) to show connections.
  - Stops when there’s no next node (None).

---

```python
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
```
- **Purpose:** To add a new node at the end of the list.
- **How:**
  - A new Node is created with the given data.
  - If the list is empty (head is None), the new node becomes the head.
  - Otherwise, it traverses to the last node and links it to the new node.

---

```python
    def delete_node(self, key):
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
```
- **Purpose:** To remove a node that contains a specific value.
- **How:**
  - If the node to delete is the head, move the head to the next node.
  - Otherwise, find the node with the given key and link the previous node to the next one.
  - If the value isn’t found, display a message.

---

```python
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"{key} found in the list.")
                return True
            current = current.next
        print(f"{key} not found in the list.")
        return False
```
- **Purpose:** To find whether a given value exists in the list.
- **How:**
  - Starts from the head and checks each node’s data.
  - If it matches the key, it prints a message and returns True.
  - If it reaches the end without finding it, prints “not found”.

---

```python
ll = LinkedList()
```
- **Purpose:** To create an empty linked list that can hold nodes.
- **How:**
  - Calls the LinkedList constructor.
  - The head starts as None.

---

```python
ll.insert_end(5)
ll.insert_end(15)
ll.insert_end(25)
ll.insert_end(35)
ll.display()
```
- **Purpose:** To add elements to the list and show the result.
- **How:**
  - Adds 5, 15, 25, and 35 at the end one by one.
  - The display() shows: 5 -> 15 -> 25 -> 35 -> None

---

```python
ll.delete_node(15)
ll.display()
```
- **Purpose:** To remove a node with the value 15.
- **How:**
  - Finds the node with data = 15 and removes it from the chain.
  - After deletion: 5 -> 25 -> 35 -> None

---

```python
ll.search(25)
```
- **Purpose:** To check if 25 exists in the list.
- **How:**
  - Traverses the list until it finds 25.
  - Prints: 25 found in the list.

---

```python
ll.display()
```
- **Purpose:** To show the final state of the linked list.
- **How:**
  - Prints the remaining elements: 5 -> 25 -> 35 -> None

---

### Summary

- Node: holds the data and link to the next node.
- LinkedList: manages all nodes through head.
- insert_end(): adds a node at the end.
- delete_node(): removes a node by value.
- search(): checks if a value exists.
- display(): prints the linked list visually.