<div align="center">

# Exercise #2 — Insertion Variations

## 📘 Overview
This exercise demonstrates how to perform **different types of insertions** in a **singly linked list** using Python.  
It builds on the basic linked list structure by introducing:
- **Insertion at the beginning** of the list.
- **Insertion after a specific node** in the list.

Through this exercise, you’ll understand how node connections are dynamically managed in memory and how inserting elements affects the structure of a linked list.

---

## ⚙️ How the Code Works

### 1. `insert_beginning(data)`
**Purpose:**  
To insert a new node at the **start** of the linked list.

**How:**
1. A new node is created using the provided `data`.
2. The new node’s `next` pointer is linked to the current head of the list.
3. The list’s `head` is updated to the new node, making it the first element.

### 2. `insert_after(prev_data, data)`
**Purpose:**  
To insert a new node **after a specific existing node** (identified by its data value).

**How:**
1. The list is traversed until the node containing `prev_data` is found.
2. A new node is created and inserted right after the found node.
3. The `next` pointers are adjusted so the new node fits correctly into the sequence.
 
### 3. Test Both Methods and Display the List
**Purpose:**  
To verify that both insertion methods (`insert_beginning()` and `insert_after()`) work correctly and modify the linked list as intended.

**How:**
1. Create an initial linked list using `insert_end()`.  
2. Insert a node at the beginning and display the updated list.  
3. Insert another node after a specific node and display the final list.

## 🧠 Summary
This exercise shows how linked lists allow **flexible insertion** without rearranging all elements (unlike arrays).  
By adding `insert_beginning()` and `insert_after()`:
- You can easily insert nodes **at any point** in the list.  
- It demonstrates how **pointer manipulation** controls data organization dynamically.

These insertion techniques are fundamental to understanding **dynamic data structures** and will be useful for more advanced linked list operations such as deletion, searching, and reversal.


