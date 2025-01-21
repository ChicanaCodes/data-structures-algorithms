# 🌟 Linked Lists: Introduction and Basics 🌟

# 💡 What is a Linked List?
# A linked list is a data structure where each element (called a node) contains:
# 1. Data: The value stored in the node.
# 2. Pointer: A reference to the next node in the list (or None for the last node).

# 🔧 Creating a Node Class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data in the node
        self.next = None  # Pointer to the next node, initially None

# 🚀 Creating a Linked List
# Let's create nodes for a linked list containing 1, 2, and 3.
head = Node(1)  # First node (head)
second = Node(2)  # Second node
third = Node(3)  # Third node

# Linking the nodes together
head.next = second  # Link first node to second
second.next = third  # Link second node to third

# 🔄 Traversing the Linked List
# We traverse the list by following the 'next' pointers.
def traverse_linked_list(head):
    current = head
    while current:
        print(current.data, end=" 🤯 ")  # Print data with a fun emoji
        current = current.next
    print("null")  # Indicate the end of the list

# Traverse the linked list
print("Linked List:")
traverse_linked_list(head)