class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BST:
    def __init__(self, data):
        self.head = data
        self.left = None
        self.right = None
        
    def append_left(self, data):
        self.head.left = data
        
    def append_right(self, data):
        self.head.right = data
        
    