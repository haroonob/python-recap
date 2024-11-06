# String Initialization
my_string = "  Hello, Python World!  "

# 1. String length
print("Length of string:", len(my_string))  # Output: 24

# 2. String strip() - Remove leading and trailing whitespaces
stripped_string = my_string.strip()
print("String after stripping whitespaces:", stripped_string)  # Output: "Hello, Python World!"

# 3. String case conversion
print("String in uppercase:", my_string.upper())  # Output: "  HELLO, PYTHON WORLD!  "
print("String in lowercase:", my_string.lower())  # Output: "  hello, python world!  "
print("String with title case:", my_string.title())  # Output: "  Hello, Python World!  "

# 4. String replacement
replaced_string = my_string.replace("Python", "Java")
print("String after replacing 'Python' with 'Java':", replaced_string)  # Output: "  Hello, Java World!  "

# 5. String slicing
print("Substring from index 7 to 13:", my_string[7:14])  # Output: "Python"
print("Substring from index -6 to end:", my_string[-6:])  # Output: "World!  "

# 6. String split
split_string = my_string.split(", ")
print("String after splitting by ', ':", split_string)  # Output: ['  Hello', 'Python World!  ']

# 7. String join
joined_string = "-".join(["Python", "is", "awesome"])
print("String after joining with '-':", joined_string)  # Output: "Python-is-awesome"

# 8. String find() and rfind()
find_result = my_string.find("Python")
print("Index of 'Python' in string:", find_result)  # Output: 7
rfind_result = my_string.rfind("World")
print("Last index of 'World' in string:", rfind_result)  # Output: 18

# 9. String format() - Using the format method for string formatting
name = "Alice"
age = 30
greeting = "My name is {} and I am {} years old.".format(name, age)
print("Formatted string using format():", greeting)  # Output: "My name is Alice and I am 30 years old."

# 10. f-strings (Python 3.6+)
greeting_fstring = f"My name is {name} and I am {age} years old."
print("Formatted string using f-string:", greeting_fstring)  # Output: "My name is Alice and I am 30 years old."

# 11. String concatenation
concatenated_string = my_string + " Have a great day!"
print("Concatenated string:", concatenated_string)  # Output: "  Hello, Python World!  Have a great day!"

# 12. Checking if a substring is present
contains_python = "Python" in my_string
print("Does the string contain 'Python'? :", contains_python)  # Output: True

# 13. String comparison
comparison_result = "apple" == "banana"
print("Is 'apple' equal to 'banana'? :", comparison_result)  # Output: False

# 14. String startswith() and endswith()
starts_with_hello = my_string.startswith("  Hello")
print("Does the string start with '  Hello'? :", starts_with_hello)  # Output: True

ends_with_world = my_string.endswith("World!  ")
print("Does the string end with 'World!  '? :", ends_with_world)  # Output: True

# 15. Checking if the string is alphanumeric
is_alphanumeric = "Python3".isalnum()
print("Is 'Python3' alphanumeric? :", is_alphanumeric)  # Output: True

# 16. String alignment (center, left, right)
aligned_string = "Python".center(20, "-")
print("String after center alignment:", aligned_string)  # Output: "---Python------"
aligned_left = "Python".ljust(20, "-")
print("String after left alignment:", aligned_left)  # Output: "Python------------"
aligned_right = "Python".rjust(20, "-")
print("String after right alignment:", aligned_right)  # Output: "------------Python"

# 17.
