import json
import os

tasks = []

def add_task(description):
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"ID: {task['id']} - {task['description']} - {status}")

def update_task(task_id, description=None, completed=None):
    for task in tasks:
        if task["id"] == task_id:
            if description:
                task["description"] = description
            if completed is not None:
                task["completed"] = completed
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print("Task deleted successfully!")

def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!")

def load_tasks(filename="tasks.json"):
    global tasks
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully!")
    else:
        print("No saved tasks found.")

def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description (leave blank to skip): ")
            completed = input("Mark as completed? (yes/no/leave blank to skip): ")
            update_task(task_id, description or None, completed.lower() == "yes" if completed else None)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            load_tasks()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
