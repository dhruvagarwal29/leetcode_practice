"""
Any object that can be given to a with statement in Python is a context manager.
Context managers define an entrance step and an exit step which are run
automatically when the with block is entered and exited.
"""


class ContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self,exe_type,exe_value,traceback):
        print("Exiting context")
    
with ContextManager() as context:
    print("Inside context")
