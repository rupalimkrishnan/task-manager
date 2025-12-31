import json
TASKS_FILE = "tasks.json"

def load_tasks():
    global tasks
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks()   # Save after adding
    print("Task added successfully!")

def list_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks()  # Save after deleting
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
