class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
   
    if root=None:
        root=BinaryTreeNode(new_value)
        retuen root
        
    else:
        if new_value < root:
            if root.left_child==None:
                root.left_child=BinaryTreeNode(new_value)
            else:
                insert(root.left_child,new_value)
        else:
             if root.left_child==None:
                root.left_child=BinaryTreeNode(new_value)
            else:
                insert(root.left_child,new_value)
            
      


def inorder(root) -> None:
    if root== None:
        print("")
    inorder(root.left)
    inorder(root.data)
    inorder(root.right)

def preorder(root) -> None:
    if root=None:
        print("")
    preorder(root.data)
    preorder(root.left)
    preorder(root.right)
    

def postorder(root) -> None:
     if root=None:
        print("")
    postorder(root.left)
    postorder(root.right)
    postorder(root.data)


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
