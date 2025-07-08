class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"

    def __str__(self):
        return str(self.value)
    
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0

    def __repr__(self):
        return f"Tree(size={self.size}, height={self.height})"

    def __str__(self):
        return f"Tree with root: {self.root}" if self.root else "Empty Tree"