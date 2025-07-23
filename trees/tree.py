class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return f"TreeNode({self.value})"

    def __str__(self):
        return str(self.value)

    def insert(self, parent_value, new_value):
        if self.value == parent_value:
            self.children.append(TreeNode(new_value))
            return True
        for child in self.children:
            if child.insert(parent_value, new_value):
                return True
        return False

    def remove(self, target_value):
        if self.value == target_value:
            return False
        for i, child in enumerate(self.children):
            if child.value == target_value:
                self.children.pop(i)
                return True
        for child in self.children:
            if child.remove(target_value):
                return True
        return False

    def print_tree(self, level=0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.print_tree(level + 1)


root = TreeNode("Root")
root.insert("Root", "Documents")
root.insert("Documents", "resume.pdf")
root.insert("Documents", "photo.jpg")
root.insert("Root", "Music")
root.insert("Music", "90s")
root.insert("90s", "nirvana.mp3")

root.print_tree()

root.remove("nirvana.mp3")
root.insert("90s", "britney.mp3")
root.print_tree()

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0

    def __repr__(self):
        return f"Tree(size={self.size}, height={self.height})"

    def __str__(self):
        return f"Tree with root: {self.root}" if self.root else "Empty Tree"
