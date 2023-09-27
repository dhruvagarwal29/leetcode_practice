class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x , self.y + other.y)
        else:
            raise ValueError("Can only add two point objects ")
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(1,2)
point2 = Point(3,5)

result = point1 + point2  ## The __add__ method of point1 is invoked here

print(result)  # The __str__ method of the point object is invoked here