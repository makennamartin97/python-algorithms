# LIFO - last in first out
# append and pop
class Stack: 

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use peek to look at the top of the stack

    def peek(self):     
	    return self.stack[-1]
    
    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            print("No element in stack")
        else:
            return self.stack.pop()

stack1 = Stack()
stack1.add("Mon")
stack1.add("Tue")
print(stack1.peek())
stack1.add("Wed")
stack1.add("Thu")
stack1.remove()
print(stack1.peek())