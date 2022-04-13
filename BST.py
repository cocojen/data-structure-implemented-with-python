class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)
            
    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)        
                
    
    def get_min(self):
        if self.node:
            return self.get_min_value(self.root)
    
    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)
        
        return node.data
        
    def get_max(self):
        if self.node:
            return self.get_max_value(self.root)
        
    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)
        
        return node.data
    
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)
            
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)
        
        if node.right_node:
            self.traverse_in_order(node.right_node)