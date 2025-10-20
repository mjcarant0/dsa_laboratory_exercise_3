<div align="center">

# Exercise #2

</div>

## Insertion Variations

### Overview

A **singly linked list** is a type of data structure where each node holds data and a link to the next node.
This exercise demonstrates **inserting a new node at the beginning** of the list and **inserting a new node after a specific node**.

### How the Code Works

#### 1. **Node Class**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

**Purpose:** To represent a single node in the linked list.

**How:**

- self.data stores the node’s data.
- self.next stores the reference (link) to the next node.
- Initially, self.next is set to None since the node isn’t linked yet.

#### 2. LinkedList Class

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

**Purpose:** To manage and control all the nodes in the list.

**How:**

- self.head is the first node (the entry point of the list).
- It starts as None since the list is empty at creation.

#### 3. Display All Nodes

```python
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```
**Purpose:** To visually show how the nodes are connected.

**How:**

- Starts from the head and moves node by node.
- Prints each node’s data followed by an arrow (->).
- Stops when there are no more nodes (None).

#### 4. Insert a Node at the 

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

**Purpose:** To add a new node to the end of the list.

**How:**

- Creates a new node using the provided data.
- If the list is empty, the new node becomes the head.
- Otherwise, it loops until the last node and links it to the new one.

#### 5. Insert a Node at the Beginning

```python
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
```

**Purpose:** To add a new node before the current head.

**How:**

- A new node is created.
- The new node’s next points to the current head.
- The head is then updated to this new node.

Result: The new node becomes the first element of the list.

#### 6. Insert a New Node After a Specific Node

```python
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
```

**Purpose:** To insert a new node after a node with specific data.

**How:**

- Traverses the list until it finds the node with the target data (prev_data).
- If not found, prints an error message.
- Otherwise, links the new node between the target node and the next node.

#### Test Implementation
```python
# Create a LinkedList object
ll = LinkedList()

# Insert nodes at the end
ll.insert_end(11)
ll.insert_end(88)

print("Linked List after inserting at the end:")
ll.display()

# Insert a node at the beginning
print("\nInsert at the beginning:")
ll.insert_beginning(77)
ll.display()

# Insert a node after a specific node
print("\nInsert after a specific node:")
ll.insert_after(11, 55)
ll.display()
```

#### Output Example

```python
Linked List after inserting at the end:
11 -> 88 -> None

Insert at the beginning:
77 -> 11 -> 88 -> None

Insert after a specific node:
77 -> 11 -> 55 -> 88 -> None
```

### Summary

- insert_end() → Adds a new node at the end of the list.
- insert_beginning() → Adds a node before the current head.
- insert_after() → Inserts a node after a specific value.
- display() → Prints the list in order.

This exercise helps demonstrate how pointer manipulation works in linked lists by changing node connections dynamically.