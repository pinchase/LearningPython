import os  # For file handling

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from a file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "completed": status == "True"})
    return tasks

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['task']} [{status}]")
    print()

def add_task(tasks):
    """Add a new task."""
    new_task = input("Enter the new task: ")
    tasks.append({"task": new_task, "completed": False})
    print(f"Task '{new_task}' added successfully!")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task '{tasks[task_number - 1]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List Manager."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_completed(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                save_tasks(tasks)
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
