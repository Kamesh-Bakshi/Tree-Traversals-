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
# function for inorder order traversing without recursion or using stack
def Morristraversal(root):
    cur = root
    while cur:
        #if left subtree exist
        if cur.left is None:
            print(cur.data)
            cur = cur.right
        else:
            #finding inorder predecessor
            pred = cur.left
            while pred.right is not None and pred.right != cur:
                pred = pred.right
            #linking root to inorder predecessor 
            if pred.right is None:
                pred.right = cur
                cur = cur.left
            #breaking link between predecessor and root
            else:
                pred.right = None
                print(cur.data)
                cur = cur.right
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
Morristraversal(root)
# Morristraversal => 7 15 18 20 52 78
