FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted.")
    except:
        print("Invalid input.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()