class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0