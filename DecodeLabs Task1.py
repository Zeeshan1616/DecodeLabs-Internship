print("\nWelcome to the To Do List")
print("Where you make your routine\n")
tasks = []

def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.\n")

def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        print()

def main():
    while True:
        print("---- TO-DO LIST MENU ----")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Thankyou for using the To Do List!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()