class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        temp = Node(data)
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = temp
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = temp
                else:
                    self.right.insert(data)
            else:
                self.data = data
def inorder(root):
    # if root is none return
    if root is None:
        return
    # we traverse the left subtree
    inorder(root.left)
    # print the data of root
    print(root.data)
    # last we traverse the right subtree
    inorder(root.right)
# same below in every recursive traversal function just changing the order.
def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
# example
"""
                 20
                /  \
               15   52
              /  \    \ 
             7    18   78

"""
root = Node(20)
root.insert(15)
root.insert(52)
root.insert(78)
root.insert(7)
root.insert(18)
inorder(root)
preorder(root)
postorder(root)
# inorder => 7 5 18 20 52 78
# preorder => 20 15 7 18 52 78
# postorder => 7 18 15 78 52 20
