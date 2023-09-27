"""
__str__
__repr__

"""

class Test:
    def __init__(self, value):
        self.value = value

    def __del__(self):
        print("object deleted ")

    def __str__(self):
        return f"Test class Value is {self.value}"

    def __repr__(self):
        return f"{self.value}"
    
obj = Test(5)
print(str(obj))
print(type(repr(obj)))
obj

"""
In nutshell __str__ is for printing the string representation of the object
and __repr__ is for debugging purposes like we can check the type of the object
using the repr method

__repr__ gives the unambiguous representation of the object
"""
