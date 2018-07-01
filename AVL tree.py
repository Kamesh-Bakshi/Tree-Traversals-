class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class avl:
    def insert(self,root,key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)

        root.height = max(self.height(root.left) , self.height(root.right)) + 1
        balance = self.Balance(root)

        if balance > 1 and key < root.left.val:
            
            return self.rightRotate(root)
 
        
        if balance < -1 and key > root.right.val:
            
            return self.leftRotate(root)
 
        
        if balance > 1 and key > root.left.val:
            
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        
        if balance < -1 and key < root.right.val:
            
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def delete(self,root,key):
        if root is None:
            return root
        if key < root.val:
            root.left=self.delete(root.left,key)
        elif key > root.val:
            root.right=self.delete(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=temp
                return temp
            cur = root.right
            while cur.left is not None:
                cur=cur.left
            temp = cur
            root.val=temp.val
            root.right=self.delete(root.right,temp.val)

        root.height = max(self.height(root.left) , self.height(root.right)) + 1
        balance = self.Balance(root)

        if balance > 1 and key < root.left.val:
            
            return self.rightRotate(root)
 
        
        if balance < -1 and key > root.right.val:
            
            return self.leftRotate(root)
 
        
        if balance > 1 and key > root.left.val:
          
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        
        if balance < -1 and key < root.right.val:
            
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
        
    def leftRotate(self,z):
        y=z.right
        t = y.left
        y.left=z
        z.right=t
        z.height= max(self.height(z.left),self.height(z.right)) + 1
        y.height= max(self.height(y.left),self.height(y.right)) + 1
        return y
    def rightRotate(self,z):
        y=z.left
        t=y.right
        y.right=z
        z.left=t
        z.height= max(self.height(z.left),self.height(z.right)) + 1
        y.height= max(self.height(y.left),self.height(y.right)) + 1
        return y
    def height(self,root):
        if not root:
            return 0
        return root.height
    def Balance(self,root):
        if not root:
            return 0
        return self.height(root.left) - self.height(root.right)
    def preorder(self,root):
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

tree = avl()
root = None
root = tree.insert(root,10)
root = tree.insert(root,20)
root = tree.insert(root,30)
root = tree.insert(root,40)
root = tree.insert(root,35)
root = tree.insert(root,25)
tree.preorder(root)
root = tree.delete(root,35)
tree.preorder(root)
