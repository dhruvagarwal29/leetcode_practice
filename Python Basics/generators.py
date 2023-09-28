"""
Genrators in Python are a way to create iterators.
Generators are functions that return an iterable object.

Generators in Python provide a convenient way to 
work with sequences of data in a memory-efficient and 
iterable manner. They are created using functions or 
expressions containing yield statements and are particularly 
useful for handling large or dynamically generated datasets.
"""

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

for value in gen:
    print(value)

## next function in generators
# print(next(gen))