# implementation
# create root 
# We just create a Node class and add assign a value to the node. This 
# becomes tree with only a root node.

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    
    # Inserting into a Tree
    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()



root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)

root.printtree()