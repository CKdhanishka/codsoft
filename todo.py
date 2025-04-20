import os

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks, new_task):
    new_task = new_task.strip()
    if new_task:
        tasks.append(new_task)
        print("Task Added Successfully.")
    else:
        print("Task cannot be empty.")

def update_task(tasks, index, updated_task):
    if 1 <= index <= len(tasks):
        updated_task = updated_task.strip()
        if updated_task:
            tasks[index - 1] = updated_task
            print("Task Updated Successfully.")
        else:
            print("Updated task cannot be empty.")
    else:
        print("Invalid Task Index.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        confirm = input(f"Are you sure you want to delete task {index}? (y/n): ")
        if confirm.lower() == 'y':
            deleted_task = tasks.pop(index - 1)
            print(f"Task '{deleted_task}' deleted Successfully.")
        else:
            print("Delete cancelled.")
    else:
        print("Invalid Task Index.")

def save_task_to_file(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_tasks_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            tasks = file.read().splitlines()
    return tasks

# Optional: Search feature
# def search_tasks(tasks, keyword):
#     results = [task for task in tasks if keyword.lower() in task.lower()]
#     if results:
#         print("\nSearch Results:")
#         for i, task in enumerate(results, 1):
#             print(f"{i}. {task}")
#     else:
#         print("No matching tasks found.")

def main():
    file_path = "todo_list.txt"
    tasks = load_tasks_from_file(file_path)

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n===== To-Do List =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        # print("6. Search Tasks")  # Optional search feature
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter the task to add: ")
            add_task(tasks, new_task)

        elif choice == "3":
            try:
                index = int(input("Enter the task index to update: "))
                updated_task = input("Enter the updated task: ")
                update_task(tasks, index, updated_task)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                index = int(input("Enter the task index to delete: "))
                delete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            save_task_to_file(file_path, tasks)
            print("Tasks saved. Exiting...")
            break

        # Optional search
        # elif choice == "6":
        #     keyword = input("Enter keyword to search: ")
        #     search_tasks(tasks, keyword)

        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()