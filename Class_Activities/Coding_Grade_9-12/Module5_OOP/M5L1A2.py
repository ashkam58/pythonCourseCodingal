# M5L1A2: Class Vehicle
# Activity 2: Working with __init__ Constructor Method and Instance Attributes

# create class
class Vehicle:
    # create init method
    def __init__(self, max_speed, mileage):
        # bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
modelX = Vehicle(240, 18)

# access the variables inside init method
print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)
