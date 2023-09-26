def my_args(*args):
    print(args[1])

my_args("heelo", "hi1", "dhruv")

def my_kwargs(**kwargs):
    print(kwargs["name"], kwargs["age"])

my_kwargs(name="dhruv", age=23)