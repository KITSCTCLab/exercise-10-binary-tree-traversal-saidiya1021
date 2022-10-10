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
    new_value=BinaryTreeNode(data)
    if self.left_child == None and self.right_child == None:
        root=new_value
        
    else:
        while new_value <= root:
            self.left_child=new_value
            
        while new_value >= root:
            self.right_child=new_value
    return root


def inorder(root) -> None:
    for i in range(len(self.left_child)):
        print(i,endl=',')
    print(root,endl=',')
    for i in range(len(self.right_child)):
        print(i,endl=',')


def preorder(root) -> None:
    print(root,endl=',')
    for i in range(len(self.left_child)):
        print(i,endl=',')
     for i in range(len(self.right_child)):
        print(i,endl=',')


def postorder(root) -> None:
    for i in range(len(self.left_child)):
        print(i,endl=',')
     for i in range(len(self.right_child)):
        print(i,endl=',')
     print(root,endl=',')


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
