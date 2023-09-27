"""
__len__(self): Called by len(object) to get the length of an object.
__getitem__(self, key): Called for indexing, e.g., object[key].
__setitem__(self, key, value): Called when setting a value via indexing, e.g., object[key] = value.
__delitem__(self, key): Called when an item is deleted using del object[key].
__iter__(self): Called to create an iterator object for the container.
__next__(self): Used to iterate over container elements.
"""

class Container:
    def __init__(self) -> None:
        self.data = []
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __str__(self):
        return str(self.data)

con = Container()

con.data = [1,2,3]
con.__setitem__(0,5)
print(con)
print(con.__getitem__(2))
