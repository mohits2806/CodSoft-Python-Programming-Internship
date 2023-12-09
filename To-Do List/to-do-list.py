# User Defined Fuctions
def display_menu():
    print("**Your To-Do List**")
    print("To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def your_tasks(tasks):
    print("\n**Your Tasks**")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"\nTask '{new_task}' added successfully to your To-Do List.\n")

def complete_task(tasks, task_name):
    if task_name in tasks:
        completed_task_index = tasks.index(task_name)
        tasks[completed_task_index] = f"✓ {task_name}"
        print(f"\nTask '{task_name}' marked as completed.\n")
    else:
        print(f"\nTask '{task_name}' not found.\n")

def delete_task(tasks, task_name):
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"\nTask '{task_name}' deleted successfully.\n")
    else:
        print(f"\nTask '{task_name}' not found.\n")

# Main Program 
tasks = []
while(1):
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        your_tasks(tasks)
    elif choice == '2':
        new_task = input("Enter the new task: ")
        add_task(tasks, new_task)
    elif choice == '3':
        task_name = input("Enter the task name to mark as completed: ")
        complete_task(tasks, task_name)
    elif choice == '4':
        task_name = input("Enter the task name to delete: ")
        delete_task(tasks, task_name)
    elif choice == '5':
        print("Thank you for using our To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")