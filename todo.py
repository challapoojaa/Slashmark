tasks = []

while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['task']} ({status})")
    elif choice == '2':
        task_name = input("Enter the task: ")
        task = {"task": task_name, "completed": False}
        tasks.append(task)
        print(f"Task '{task_name}' added to your to-do list.")
    elif choice == '3':
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['task']} ({status})")

            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print(f"Task {task_number} marked as completed.")
            else:
                print("Invalid task number. Please enter a valid task number.")
        else:
            print("Your to-do list is empty.")
    elif choice == '4':
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['task']} ({status})")

            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' removed from your to-do list.")
            else:
                print("Invalid task number. Please enter a valid task number.")
        else:
            print("Your to-do list is empty.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
