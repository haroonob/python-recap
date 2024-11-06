# Initialize an empty list to store the todo items
todo_list = []

print("Enter a task for your todo list. Press <enter> when done:")

while True:
    # Prompt the user for a task
    task = input("> ")

    # Check if the user entered a blank input
    if task == "":
        break  # Exit the loop if the input is blank

    # Add the task to the list and confirm it was added
    todo_list.append(task)
    print("Task added.")

# Display the completed todo list
print("\nYour ToDo List:")
for task in todo_list:
    print("-", task)
