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
# function for level order traversing
def levelorder(root):
    #implement a queue
    queue = []
    #add root node to queue
    queue.append(root)
    #loop until queue is empty
    while queue:
        temp = queue.pop(0)
        print(temp.data)
        #add left child of node to queue
        if temp.left is not None:
            queue.append(temp.left)
        #add right child of node to queue
        if temp.right is not None:
            queue.append(temp.right)
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
levelorder(root)
# levelorder => 20 15 52 7 18 78
