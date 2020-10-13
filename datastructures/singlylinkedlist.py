class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next
    
    def insertatHead(self,newdata):
        newnode = Node(newdata)
        # Update the new nodes next value to the existing node
        newnode.next = self.head
        self.head = newnode


    def insertatTail(self, newdata):
        newnode = Node(newdata)
        # check if its empty
        if self.head is None:
            self.head = newnode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = newnode

    # Inserting in between two Data Nodes
    # This involves chaging the pointer of a specific node to point to the 
    # new node. That is possible by passing in both the new node and the 
    # existing node after which the new node will be inserted.

    def inbetween(self, middlenode, newdata):
        if middlenode is None:
            print("The middle node is absent")
        newnode = Node(newdata)
        # set newnodes next val to the middlenodes next val, then middlenode 
        # next val to the newnode
        newnode.next = middlenode.next
        middlenode.next = newnode

    # We can remove an existing node using the key for that node. In the 
    # below program we locate the previous node of the node which is to 
    # be deleted. Then point the next pointer of this node to the next node 
    # of the node to be deleted.
    def removenode(self, removenode):
        curr = self.head
        if curr is not None:
            if curr.data == removenode:
                self.head = curr.next
                curr = None
                return
        while curr is not None:
            if curr.data == removenode:
                break
            prev = curr
            curr = curr.next
        if curr == None:
            return
        prev.next = curr.next
        curr = None






list1 = SLL()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3

# list1.insertatHead("Sun")
list1.insertatTail("Thurs")
list1.insertatTail("Fri")
list1.inbetween(list1.head.next, "Sat")
list1.removenode("Sat")

list1.listprint()