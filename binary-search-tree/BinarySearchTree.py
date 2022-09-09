from collections import deque
from tkinter.tix import Tree
from Node import Node

class BST:
    
    def __init__(self, root: Node = None):
        self.root = root
        
    def isEmpty(self):
            return self.root is None
    
    def insert(self, x):
        self.root = self._insert(self.root, x)
    
    def _insert(self, p: Node, x):
        if p is None:
            p = Node(x)
        if x < p.data:
            p.left = self._insert(p.left, x)
        elif x > p.data:
            p.right = self._insert(p.right, x)
        else:
            print("Value is already present in tree")
            return
        return p
    
    def insert1(self, x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.data:
                p = p.left
            elif x > p.data:
                p = p.right
            else:
                print("Value is already present in the tree.")
                return
        temp = Node(x)
        if par is None:
            par = temp
        elif x < par.data:
            par.left = temp
        else:
            par.right = temp
    
    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, p: Node, x):
        if p is None:
            print(x, "is not present in the tree")
            return p
        if x < p.data:
            p.left = self._delete(p.left, x)
        elif x > p.data:
            p.right = self._delete(p.right, x)
        else:
            if p.left is not None and p.right is not None:
                s: Node = p.right
                while s.left is not None:
                    s = s.left
                p.data = s.data
                p.right = self._delete(p.right, s.data)
            else:
                if p.left is not None:
                    ch = p.left
                else:
                    ch = p.right
                p = ch
        return p
        
    def delete1(self, x):
        p = self.root
        par = None
        
        while p is not None:
            if x == p.data:
                break
            elif x < p.data:
                p = p.left
            else:
                p = p.right
                
        if p is None:
            return "Value doesn't found in the tree"
        
        if p.left is not None and p.right is not None:
            ps = p
            s: Node = p.right
            while s.left is not None:
                ps = s
                s = s.left
            p.data = s.data
            p = s
            par = ps
            
        if p.left is not None:
            ch = p.left
        else:
            ch = p.right
            
        if par is None:
            self.root = ch
        elif p == par.left:
            par.left = ch
        else:
            par.right = ch
    
    def search(self, x):
        return self._search(self.root, x) is not None
    
    def _search(self, p: Node, x):
        if p is None:
            return None
        if x < p.data:
            return self._search(p.left, x)
        if x > p.data:
            return self._search(p.right, x)
        return p
    
    def search1(self, x):
        p = self.root
        while p is not None:
            if x < p.data:
                p = p.left
            elif x > p.right:
                p = p.right
            else:
                return True
        return False
    
    def min(self):
        if self.isEmpty():
            return "Tree is empty"
        return self._min(self.root)
    
    def _min(self, p: Node):
        if p.left is None:
            return p
        return self._min(p.left)
    
    def max(self):
        if self.isEmpty():
            return "Tree is empty"
        return self._max(self.root)
    
    def _max(self, p: Node):
        if p.right is None:
            return p
        return self._max(p.right)
    
    def min1(self):
        if self.isEmpty():
            return "Tree is empty"
        p = self.root
        while p.left is not None:
            p = p.left
        return p.data
    
    def max1(self):
        if self.isEmpty():
            return "Tree is empty"
        p = self.root
        while p.right is not None:
            p = p.right
        return p.data
    
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
        
    def sum(self):
        return self._sum(self.root)
    
    def _sum(self, p: Node):
        if p is None:
            return 0
        return (p.data + self._sum(p.left) + self._sum(p.right))

    def distanceOfANode(self, root: Node, a):
        if root == None:
            return 0
        if a < root.data:
            return 1 + self.distanceOfANode(root.left, a)
        return 1 + self.distanceOfANode(root.right, a)
    
    def distanceOfTwoNodes(self, root: Node, a, b):
        if root == None:
            return 0
        
        if a < root.data and b < root.data:
            return self.distanceOfTwoNodes(root.left, a, b)
        
        if a > root.data and b > root.data:
            return self.distanceOfTwoNodes(root.right, a, b)
        
        if a <= root.data and b >= root.data:
            return (self.distanceOfANode(root.left, a)+self.distanceOfANode(root.right, b))
        
        