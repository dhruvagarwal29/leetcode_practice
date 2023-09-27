"""
__init__ 
__del__
"""

class Test:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("object deleted ")

obj = Test()
del obj