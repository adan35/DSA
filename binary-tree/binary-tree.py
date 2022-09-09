from node import Node
from collections import deque

class BinaryTree:
    
    def __init__(self, root: Node = None):
        self.root = root
       
    def isEmpty(self):
        return self.root is None
    
    def preOrder(self):
        self._preOrder(self.root)
        print()
    
    def _preOrder(self, root: Node):
        if root is None:
            return
        print(root.data, end=' ')
        self._preOrder(root.left)
        self._preOrder(root.right)
        
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self,  root: Node):
        if root is None:
            return
        self._inorder(root.left)
        print(root.data, end=' ')
        self._inorder(root.right)
        
    def postOrder(self):
        self._postOrder(self.root)
        print()
    
    def _postOrder(self, root: Node):
        if root is None:
            return
        self._postOrder(root.left)
        self._postOrder(root.right)
        print(root.data, end=' ')
        
    def level_order(self):
        if self.root is None:
            print("Tree is empty")
            return
        d = deque()
        d.append(self.root)
        while len(d) != 0:
            p: Node = d.popleft()
            print(p.data, end=' ')
            if p.left is not None:
                d.append(p.left)
            if p.right is not None:
                d.append(p.right)
                
    def height(self):
        self._height(self.root)

    def _height(self, root: Node):
        if root is None:
            return 0

        hl = self._height(root.left)
        hr = self._height(root.right)

        if hl > hr:
            return 1 + hl
        else:
            return 1 + hr
        
    def create_tree(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        
b = BinaryTree()
b.create_tree()
b.inorder()
        
    