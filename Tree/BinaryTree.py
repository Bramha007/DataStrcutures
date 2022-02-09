# Binary Tree Implementation

class Node :
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
root = Node(10)

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)


def inorder(root):
    
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.value) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.value) + "->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.value) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)



print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)
