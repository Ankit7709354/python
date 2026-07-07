tasks = []

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = int(input("Choice: "))

    if choice == 1:

        task = input("Task: ")
        tasks.append(task)

    elif choice == 2:

        if len(tasks) == 0:
            print("No Tasks")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == 3:
        break

    else:
        print("Invalid Choice")