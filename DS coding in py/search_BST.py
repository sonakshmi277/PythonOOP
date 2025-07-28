class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_bst(root, val):
    if root is None or root.key == val:
        return root
    if val < root.key:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
# Build BST manually
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

# Search for a value
val = 7
found = search_bst(root, val)

if found:
    print(f"Found node with value: {found.key}")
else:
    print("Value not found in BST")
