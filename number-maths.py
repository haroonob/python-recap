import math

# 1. Numbers
integer_num = 42
float_num = 3.14159

# Printing numbers
print("Integer number:", integer_num)  # Output: 42
print("Floating point number:", float_num)  # Output: 3.14159

# 2. Math functions from the math module
print("Square root of 16:", math.sqrt(16))  # Output: 4.0
print("3 raised to the power of 2:", math.pow(3, 2))  # Output: 9.0
print("Factorial of 5:", math.factorial(5))  # Output: 120

# 3. Trigonometric functions
angle_in_radians = math.radians(45)  # Convert 45 degrees to radians
print("Cosine of 45 degrees:", math.cos(angle_in_radians))  # Output: 0.7071067811865476
print("Sine of 45 degrees:", math.sin(angle_in_radians))  # Output: 0.7071067811865475

# 4. Absolute value
negative_number = -100
print("Absolute value of -100:", abs(negative_number))  # Output: 100

# 5. Rounding numbers
print("Rounded value of 3.14159 to 2 decimal places:", round(float_num, 2))  # Output: 3.14

# 6. Generating random numbers (import random for this)
import random
print("Random number between 1 and 100:", random.randint(1, 100))  # Output: Random number in range [1, 100]

# 7. Boolean data type
is_active = True
is_closed = False

print("is_active:", is_active)  # Output: True
print("is_closed:", is_closed)  # Output: False

# 8. Boolean comparisons
a = 10
b = 20

# Equality comparison
print("Is a equal to b?", a == b)  # Output: False

# Inequality comparison
print("Is a not equal to b?", a != b)  # Output: True

# Greater than comparison
print("Is a greater than b?", a > b)  # Output: False

# Less than comparison
print("Is a less than b?", a < b)  # Output: True

# 9. Logical operations (AND, OR, NOT)
print("True AND False:", True and False)  # Output: False
print("True OR False:", True or False)  # Output: True
print("NOT True:", not True)  # Output: False

# 10. Using boolean values in conditionals
if is_active:
    print("The status is active.")  # Output: The status is active.
else:
    print("The status is inactive.")

# 11. Using math functions with boolean values
print("Is the absolute value of -100 greater than 50?", abs(-100) > 50)  # Output: True
