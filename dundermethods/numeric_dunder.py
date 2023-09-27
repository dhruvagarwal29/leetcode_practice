"""
Implementation of numeric dunder methods.

__add__(self, other): Addition (+ operator).
__sub__(self, other): Subtraction (- operator).
__mul__(self, other): Multiplication (* operator).
__truediv__(self, other): True division (/ operator).
__floordiv__(self, other): Floor division (// operator).
__mod__(self, other): Modulo (% operator).
__pow__(self, other[, modulo]): Exponentiation (** operator).
__eq__(self, other): Equality (== operator).
__ne__(self, other): Inequality (!= operator).
__lt__(self, other): Less than (< operator).
__le__(self, other): Less than or equal to (<= operator).
__gt__(self, other): Greater than (> operator).
__ge__(self, other): Greater than or equal to (>= operator).
"""

class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __sub__(self,other):
        return Number(self.value - other.value)
    
    def __mul__(self,other):
        return Number(self.value * other.value)
        
    def __truediv__(self,other):
        if other.value != 0:
            return Number(self.value / other.value)
        else:
            raise ValueError("Division by zero")
    
    def __floordiv__(self,other):
        if other.value!= 0:
            return Number(self.value // other.value)
        else:
            raise ValueError("Division by zero")
    
    def __mod__(self,other):
        if other.value != 0:
            return Number(self.value % other.value)
        else:
            raise ValueError("Modulo by zero")
        
    def __pow__(self, other, modulo = None):
        return Number(pow(self.value, other.value, modulo))

    def __eq__(self,other):
        return self.value == other.value

    def __ne__(self,other):
        return self.value != other.value

    def __le__(self,other):
        return self.value <= other.value

    def __ge__(self,other):
        return self.value >= other.value
    
    def __lt__(self,other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value

    def __str__(self) -> str:
        return str(self.value)
    
num1 = Number(10)
num2 = Number(5)

# Arithmetic operations
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
floor_div_result = num1 // num2
mod_result = num1 % num2
pow_result = num1 ** num2


print(f"Addition: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"True Division: {div_result}")
print(f"Floor Division: {floor_div_result}")
print(f"Modulo: {mod_result}")
print(f"Exponentiation: {pow_result}")

print(f"Equality: {num1 == num2}")
print(f"Inequality: {num1 != num2}")
print(f"Less than: {num1 < num2}")
print(f"Less than or equal to: {num1 <= num2}")
print(f"Greater than: {num1 > num2}")
print(f"Greater than or equal to: {num1 >= num2}")