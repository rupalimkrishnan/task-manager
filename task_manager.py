tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def list_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
