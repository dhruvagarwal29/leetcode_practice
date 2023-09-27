"""
__call__ method is used to make an object callable like a function.
"""

class MyCallable:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y

callable_obj = MyCallable(3)
result = callable_obj(5)  # Calling the object as if it were a function
print(result)