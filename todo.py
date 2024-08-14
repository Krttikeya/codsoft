#todolist in python..
def task():
    tasks = []
    print("-- TASK MANAGEMENT --")

    total_tasks = int(input("How many tasks do you wish to add? "))
    for i in range(total_tasks):
        task_name = input(f"Enter task {i + 1}: ")
        tasks.append(task_name)

    print(f"Today's tasks are: {tasks}")

    while True:
        choice = int(input("Enter\n1 - Add task\n 2 - Update\n 3 - Delete \n 4 - View\n 5 - exit\n"))
        if choice == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been added.")

        elif choice == 2:
            updated_val = input("Enter task you wish to update: ")
            if updated_val in tasks:
                index = tasks.index(updated_val)
                updated_task = input("Enter new task: ")
                tasks[index] = updated_task
                print(f"Updated task: '{updated_task}'")
            else:
                print(f"Task '{updated_val}' not found.")

        elif choice == 3:
            delete_val = input("Enter task you wish to update: ")
            if delete_val in tasks:
                index = tasks.index(delete_val)
                del tasks[index]

                print(f"deleted task: '{delete_val}'")
            else:
                print(f"Task '{delete_val}' not found.")

        elif choice == 4:
            print(f"Tasks: {tasks}")

        elif choice==5 :
            print("closing.. ")
            break
        else:
            print("Enter valid option..")


task()
