print("Welcome to Task Manager")
tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

add_task()

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def list_tasks():
    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

add_task()
list_tasks()
