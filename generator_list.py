"""
Give me a generator which can yield million numbers
"""

def my_generator():
    for i in range(1000000):
        yield i

gen = my_generator()

for value in gen:
    print(value)

for i in range(0,100000):
    print(i)