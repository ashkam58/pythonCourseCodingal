# M5L4A1: Keep It Private!
# Activity 1: Private Attributes, Private Methods, and Access Control (Inside vs Outside)

# Class creation
class myClass:
    # private variable
    __privateVar = 27
    
    # private method
    def __privMeth(self):
        print("I'm inside class myClass")
        
    # Function to print value of private variable
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)

# Object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth
