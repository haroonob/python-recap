# Creating a list
my_list = [10, 20, 30, 40, 50]

# Accessing elements using positive indexes
print("Element at index 0:", my_list[0])  # Output: 10
print("Element at index 3:", my_list[3])  # Output: 40

# Accessing elements using negative indexes
print("Element at index -1:", my_list[-1])  # Output: 50
print("Element at index -3:", my_list[-3])  # Output: 30

# Slicing a list
print("Slice from index 1 to 3:", my_list[1:4])  # Output: [20, 30, 40]
print("Slice from index -4 to -1:", my_list[-4:-1])  # Output: [20, 30, 40]

# Appending an element to the list
my_list.append(60)
print("List after appending 60:", my_list)  # Output: [10, 20, 30, 40, 50, 60]

# Inserting an element at a specific position
my_list.insert(2, 25)
print("List after inserting 25 at index 2:", my_list)  # Output: [10, 20, 25, 30, 40, 50, 60]

# Extending a list with another list
my_list.extend([70, 80])
print("List after extending with [70, 80]:", my_list)  # Output: [10, 20, 25, 30, 40, 50, 60, 70, 80]

# Removing an element by value
my_list.remove(25)
print("List after removing 25:", my_list)  # Output: [10, 20, 30, 40, 50, 60, 70, 80]

# Removing an element by index
removed_element = my_list.pop(3)
print("Removed element at index 3:", removed_element)  # Output: 40
print("List after pop:", my_list)  # Output: [10, 20, 30, 50, 60, 70, 80]

# Counting occurrences of an element
print("Occurrences of 10 in the list:", my_list.count(10))  # Output: 1

# Finding the index of an element
print("Index of 50 in the list:", my_list.index(50))  # Output: 3

# Reversing the list
my_list.reverse()
print("List after reversing:", my_list)  # Output: [80, 70, 60, 50, 30, 20, 10]

# Sorting the list in ascending order
my_list.sort()
print("List after sorting:", my_list)  # Output: [10, 20, 30, 50, 60, 70, 80]

# Creating a new list and clearing all elements from the original list
new_list = [100, 200, 300]
my_list.clear()
print("Original list after clearing:", my_list)  # Output: []

# Extending the list again
my_list.extend(new_list)
print("List after extending with [100, 200, 300]:", my_list)  # Output: [100, 200, 300]
