<div align="center">

# Exercise #1

</div>

---

## Basic Operations

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
- **Purpose:** To be added
- **How:**  
  - To be Added
  - To be Added
  - To be Added

---

```python 
class LinkedList:
    def __init__(self):
        self.head = None
```
- **Purpose:** To be added
- **How:**  
  - To be Added
  - To be Added
  - To be Added

---

```python
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

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
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

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
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

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
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

---

```python
ll = LinkedList()
```
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

---

```python
ll.insert_end(5)
ll.insert_end(15)
ll.insert_end(25)
ll.insert_end(35)
ll.display()
```
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

---

```python
ll.delete_node(15)
ll.display()
```
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

---

```python
ll.search(25)
```
- **Purpose:** To be added
- **How:**
  - To be Added
  - To be Added
  - To be Added

---

```python
ll.display()
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