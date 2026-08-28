# M5L4A2: Computer Price
# Activity 2: Encapsulation with Private Instance Attributes and Setter Methods

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price directly from outside (does not affect private attribute)
c.__maxprice = 1000
c.sell()

# using setter function (properly updates private attribute)
c.setMaxPrice(1000)
c.sell()
