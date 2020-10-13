# FIFO - first in first out

class Queue:

    #implementation
    def __init__(self):
        self.queue = list()
      
    # Insert method to add element
    def addtoq(self, dataval):
        if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
        return False

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is empty")

    def printq(self):
        for i in self.queue:
            print(i)

# create queue
q1 = Queue()
q1.addtoq("one")
q1.addtoq("two")
q1.addtoq("three")
q1.remove()
q1.printq()


    