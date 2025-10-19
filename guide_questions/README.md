<div align="center">

# Linked List Activity

</div>

## Guide Questions

### 1. **What are the advantages of using a linked list over an array?**
- A linked list offers several advantages over an array. Unlike arrays, linked lists do not require a fixed size, allowing them to grow or shrink dynamically as needed, which makes them more memory-efficient when the size of the data is unpredictable. Additionally, linked lists make it easier to insert or delete elements, as these operations do not require shifting elements like in arrays. Instead, you simply update the pointers of the nodes. This flexibility makes linked lists particularly useful for applications where frequent insertions and deletions are required. However, it is important to note that accessing elements in a linked list is slower compared to arrays, as you need to traverse the list sequentially to reach a specific element.

---

### 2. **How does a linked list manage memory differently from arrays?**
- To be added

---

### 3. **What happens if we delete the head node in a singly linked list?**
- To be added

---

### 4. **How can we modify this code to create a doubly linked list?**
- We can modify the code to create a doubly linked list by adding a prev pointer in the Node class so that each node can link to the previous node as well as the next one. The insert method should be updated to set both the next and prev pointers when adding a new node, ensuring proper connections in both directions. The delete method should also be adjusted to fix the forward and backward links after removing a node to maintain the structure of the list. Additionally, we can optionally traverse the list backward using the prev pointer.

---
