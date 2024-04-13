import os
import json
from datetime import datetime

TODO_FILE = 'todo.json'

# Function to load tasks from JSON file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    else:
        return {'tasks': []}

# Function to save tasks to JSON file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Function to display the to-do list
def display_list():
    tasks = load_tasks()['tasks']
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['description']} - Priority: {task['priority']}, Due: {task['due_date']}")
    else:
        print("Your to-do list is empty.")

# Function to add a task to the to-do list
def add_task():
    description = input("Enter task description: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks = load_tasks()
    tasks['tasks'].append({
        'description': description,
        'priority': priority,
        'due_date': due_date_str
    })
    save_tasks(tasks)
    print(f"Task '{description}' added to your to-do list.")

# Function to remove a task from the to-do list
def remove_task():
    tasks = load_tasks()['tasks']
    if tasks:
        display_list()
        task_index = int(input("Enter task number to remove: "))
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            save_tasks({'tasks': tasks})
            print(f"Task '{removed_task['description']}' removed from your to-do list.")
        else:
            print("Invalid task number. Please try again.")
    else:
        print("Your to-do list is empty.")

# Main function to run the to-do application
def main():
    while True:
        print("\n===== To-Do Application =====")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the to-do application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
