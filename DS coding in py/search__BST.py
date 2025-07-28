class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def search(val,tree):
    if (tree is None or tree.val==val):
        return tree
    elif(val<tree.val):
        return search(val,tree.left)
    else:
        return search(val,tree.right)
node=Node(3)
node.left=Node(1)
node.right=Node(4)
val=49
f=search(val,node)
if f:
    print("Yes")
else:
    print("No")