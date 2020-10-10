# In this challenge, create a class called Temple with the following attributes:

# Create three attributes: hp (this is health points) - set this to be 200 
# when the object is initialized. Also create x and y where both are set as 
# 20, 50 respectively when they are created, as well as name which should be 
# set to None in the beginning
# Create two public methods: double_x(), double_y(), which when called doubles 
# its x/y value.
# Create another public method called: changeName() where you can pass a new 
# name for the temple

class Temple:
    def __init__(self, name):
        self.hp = 200
        self.x = 20
        self.y = 50
        self.name = None
    def double_x(self):
        self.x = self.x*2
        return self.x
    def double_y(self):
        self.y = self.y*2
    def changeName(self, name):
        self.name = name
    def stats(self):
        print("Name: ", self.name)
        print("hp: ", self.hp)
        print("x: ", self.x)
        print("y: ", self.y)
 
# testing
temple1 = Temple("Mike")
temple2 = Temple("Caitlyn")
temple1.changeName("Kendall")

temple1.double_x()
temple1.double_y()
temple1.stats()