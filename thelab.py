print("Welcome to this awesome calculator you can add, subtract, multiply and divide two numbers ")
user_input = input("Enter what you want to do add(a), subtract(s), multiply(m), divide(d): ").strip().lower()

if user_input not in {"a", "s", "m", "d"}:
    print("Invalid input. Exiting program.")
    raise SystemExit

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
except ValueError:
    print("Invalid number. Exiting program.")
    raise SystemExit

#function to add two numbers
def add(a, b):
    print("addition of", a, "and", b, "is", a + b)
#function to subtract two numbers
def subtract(a, b):
    print("subtraction of", a, "and", b, "is", a - b)
#function to multiply two numbers
def multiply(a, b):
    print("multiplication of", a, "and", b, "is", a * b)
#function to divide two numbers
def divide(a, b):
    print("division of", a, "and", b, "is", a / b)

if user_input == "a":
    add(x, y)
elif user_input == "s":
    subtract(x, y)
elif user_input == "m":
    multiply(x, y)
elif user_input == "d":
    divide(x, y)