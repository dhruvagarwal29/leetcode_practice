"""
Accessing the attributes of a class
To check the attributes of a class and also to manipulate those attributes,
 we use many python in-built methods as shown below.

getattr() - A python method used to access the attribute of a class.

hasattr()  -  A python method used to verify the presence of an attribute in a class.

setattr() -  A python method used to set an additional attribute in a class.
"""


class Dhruv:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.job = "Software Engineer"
    

dhruv = Dhruv("Dhruv", 21)
print(getattr(dhruv, "name"))
print(getattr(dhruv, "job"))
print(hasattr(dhruv, "job"))
    
