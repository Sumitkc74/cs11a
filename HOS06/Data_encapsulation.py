class Computer:
    """
    Module: Data_encapsulation
    Purpose: Demonstrates data encapsulation and the use of private attributes in Python.

    This module illustrates how private attributes (prefixed with __) can be used to 
    protect class data from unauthorized external modification, and how setter methods 
    can be used to control access to those attributes.
    """

    """
    Computer class that demonstrates data encapsulation using private attributes.
    
    This class encapsulates a private attribute '__maxprice' to protect it from
    direct external modification. The class provides a public setter method
    'setMaxPrice()' as the controlled way to modify the private attribute.
    
    Attributes:
        __maxprice (int): A private attribute storing the maximum/selling price of the computer.
                            This attribute is intended to be modified only through the setMaxPrice() method.
    
    Methods:
        sell(): Displays the current selling price of the computer.
        setMaxPrice(price): Sets the maximum price of the computer through a controlled setter method.
    """

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()