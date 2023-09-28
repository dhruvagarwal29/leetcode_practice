# factorial 5! = 120 

def factorial(number):
    if number == 0:
        return 1
    elif number < 0:
        return "Factorial is undefined for negative numbers"
    else:
        return number * factorial(number - 1)

if __name__ == "__main__":
    print(factorial(5))
