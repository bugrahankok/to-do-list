import json

JSON_FILE = "tasks.json" 

def load_tasks():
    try:
        with open(JSON_FILE, "r") as f:
            global tasks
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(JSON_FILE, "w") as f:
        json.dump(tasks, f)

def add_task(description, due_date, priority):
    tasks = load_tasks()
    task = {"description": description, "due_date": due_date, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)

def view_all_tasks():
    tasks = load_tasks()
    print("All Tasks: ")
    print("******************************")
    for task in tasks:
        print("Task: ", task["description"])
        print("Due Date: ", task["due_date"])
        print("Priority: ", task["priority"])
        print("******************************")

def view_task_by_description(description):
    tasks = load_tasks()
    for task in tasks:
        if task["description"] == description:
            print("Task: ", task["description"])
            print("Due Date: ", task["due_date"])
            print("Priority: ", task["priority"])

def main():
    while True:
        print("1. Add New Task")
        print("2. Show All Tasks")
        print("3. Show Task by Name")

        choice = input("\nChoice (1-2-3): ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority level (High, Medium, Low): ")
            add_task(description, due_date, priority)
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            print("******************************")
            description = input("Enter the task description: ")
            view_task_by_description(description)
            print("******************************")
        else:
            print("Error!")
if __name__ == "__main__":
    main()
