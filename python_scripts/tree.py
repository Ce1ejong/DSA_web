# Binary Tree Implementation (python_scripts/tree.py)
# Operations: Inorder, Preorder, Postorder traversals

class Node:
    """A single node in a binary tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    """Manages the binary tree structure and traversal methods."""
    def __init__(self):
        self.root = None

    def inorder_traversal(self, root):
        """Left -> Root -> Right (Yields sorted order for a Binary Search Tree)"""
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        """Root -> Left -> Right (Used for copying/duplicating the tree)"""
        if root:
            print(root.val, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        """Left -> Right -> Root (Used for deleting the tree or expression trees)"""
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=" ")

# Example Usage:
if __name__ == "__main__":
    tree = BinaryTree()
    # Constructing a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("--- Binary Tree Traversals ---")
    print("Inorder Traversal (L R R):", end=" ")
    tree.inorder_traversal(tree.root)
    
    print("\nPreorder Traversal (R L R):", end=" ")
    tree.preorder_traversal(tree.root)
    
    print("\nPostorder Traversal (L R R):", end=" ")
    tree.postorder_traversal(tree.root)
    print("\n------------------------------")