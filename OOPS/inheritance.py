class Bird:
    def __init__(self) -> None:
        print("Bird is ready!!")
    def bird(self):
        print("Birrrrdd")
    
class Parrot(Bird):
    def __init__(self) -> None:
        super().__init__()
    def parrot(self):
        print("parrottttt")

obj = Parrot()
obj.bird()
