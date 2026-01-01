import json

TASKS_FILE = "tasks.json"

tasks = []


def load_tasks():
    """Load tasks from JSON file into memory."""
    global tasks
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    """Save current tasks list to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    """Add a new task."""
    title = input("Enter a task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return

    new_id = tasks[-1]["id"] + 1 if tasks else 1

    task = {
        "id": new_id,
        "title": title,
        "status": "pending"
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")



def list_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return

    print("Your tasks:")
    for task in tasks:
        status = "✔" if task["status"] == "done" else "✗"
        print(f'{task["id"]}. {task["title"]} [{status}]')



def delete_task():
    """Delete a task by ID."""
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks()
    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks()
                print(f'Deleted task: {task["title"]}')
                return
        print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_status():
    if not tasks:
        print("No tasks available.")
        return

    list_tasks()
    try:
        task_id = int(input("Enter task ID: "))
        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "pending":
                    task["status"] = "done"
                    print("Task marked as done.")
                else:
                    task["status"] = "pending"
                    print("Task marked as pending.")
                save_tasks()
                return
        print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number.")

def edit_task():
    if not tasks:
        print("No tasks available.")
        return

    list_tasks()
    try:
        task_id = int(input("Enter task ID to edit: "))
        for task in tasks:
            if task["id"] == task_id:
                new_title = input("Enter new task title: ").strip()
                if not new_title:
                    print("Title cannot be empty.")
                    return
                task["title"] = new_title
                save_tasks()
                print("Task updated successfully.")
                return
        print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number.")

def filter_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("1. All tasks")
    print("2. Completed tasks")
    print("3. Pending tasks")

    choice = input("Choose filter: ")

    if choice == "1":
        list_tasks()
    elif choice == "2":
        completed = [t for t in tasks if t["status"] == "done"]
        if not completed:
            print("No completed tasks.")
            return
        for task in completed:
            print(f'{task["id"]}. {task["title"]} (done)')
    elif choice == "3":
        pending = [t for t in tasks if t["status"] == "pending"]
        if not pending:
            print("No pending tasks.")
            return
        for task in pending:
            print(f'{task["id"]}. {task["title"]} (pending)')
    else:
        print("Invalid choice.")

def main():
    """Main menu loop."""
    load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Mark Task Done/Pending")
        print("5. Edit Task")
        print("6. Filter Tasks")
        print("7. Exit")


        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_status()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
