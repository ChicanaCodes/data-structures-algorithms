# 🌟 Linked List Functions in Python 🌟
# This file contains fundamental operations for Linked Lists
# including traversal, insertion, deletion, and reversal.

class Node:
    def __init__(self, data):
        self.data = data  # 📦 Store the data in the node
        self.next = None  # ➡️ Pointer to the next node (Initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # 🎯 Head points to the first node

    # 🔄 Traversing the Linked List
    def traverse(self):
        current = self.head
        while current:
            print(f"{current.data} ➡️ ", end="")
            current = current.next
        print("None")  # Marks the end of the list

    # 🆕 Inserting a Node after a given node
    def insert_after(self, prev_node, new_data):
        if not prev_node:
            print("🚨 Error: Previous node not found!")
            return
        new_node = Node(new_data)  # 📌 Create the new node
        new_node.next = prev_node.next  # 🔗 Link new node to next node
        prev_node.next = new_node  # 🔗 Link previous node to new node

    # 🗑️ Deleting a Node by Value
    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in linked list
        if not current:
            print(f"🚨 Error: Node with value {key} not found!")
            return

        prev.next = current.next  # Unlink the node from linked list
        current = None  # Free memory

    # 🔄 Reversing the Linked List
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse pointer
            prev = current  # Move prev to current node
            current = next_node  # Move to next node
        self.head = prev  # Reset head to new first node

    # 🎯 Append a New Node at the End
    def append(self, new_data):
        new_node = Node(new_data)  # 📌 Create a new node
        if not self.head:
            self.head = new_node  # If list is empty, set as head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  # 🔗 Attach new node at end

# 🔥 Example Usage
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second  # 1️⃣ → 2️⃣
second.next = third  # 2️⃣ → 3️⃣

print("🔄 Initial Linked List:")
llist.traverse()

# Adding a new node after second node
llist.insert_after(second, 4)
print("🆕 After Inserting 4 after 2:")
llist.traverse()

# Deleting a node
llist.delete_node(2)
print("🗑️ After Deleting node with value 2:")
llist.traverse()

# Reversing the list
llist.reverse()
print("🔄 After Reversing the Linked List:")
llist.traverse()

# Appending a new node
llist.append(5)
print("🎯 After Appending 5 at the End:")
llist.traverse()