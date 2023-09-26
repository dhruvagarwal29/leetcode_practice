# class Animal:
#     def __init__(self, a):
#         print(f'{a} is an animal.')

# class Mammal():
#     def __init__(self, a):
#         print(f'{a}is a warm-blooded animal.')


# class NonWingedMammal(Mammal, Animal):
#     def __init__(self, NonWingedMammalName):
#         print(NonWingedMammalName, "can't fly.")
#         super(Mammal, self).__init__("aa")
#         super(Animal, self).__init__("aa")

# obj = NonWingedMammal('Dog')

# # class Parent1:
# #     def method1(self):
# #         print("Method from Parent1")

# # class Parent2:
# #     def method2(self):
# #         print("Method from Parent2")

# # class Child(Parent1, Parent2):
# #     def __init__(self) -> None:
# #         super().__init__()

# # child = Child()
# # child.method1()
# # child.method2()  


class Animal:
    def __init__(self):
        print('is an animal.')

class Mammal():
    def __init__(self):
        print('is a warm-blooded animal.')

class NonWingedMammal(Mammal, Animal):
    def __init__(self, NonWingedMammalName):
        print(NonWingedMammalName, "can't fly.")
        super(Mammal, self).__init__()  # Call Mammal's __init__
        super(Animal, self).__init__()  # Call Animal's __init__

obj = NonWingedMammal('Dog')
