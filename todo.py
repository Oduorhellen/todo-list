def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def todo_app():
    tasks = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\n" + "=" * 35)
                print(f"{'No.':<6} | {'Task Description'}")
                print("-" * 35)
                for index, task in enumerate(tasks, start=1):
                    print(f"{index:<6} | {task}")
                print("=" * 35)
                    
        elif choice == "2":
            new_task = input("\nEnter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' added successfully.")
            else:
                print("Task cannot be empty.")
                
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to remove.")
            else:
                print("\n" + "=" * 35)
                print(f"{'No.':<6} | {'Task Description'}")
                print("-" * 35)
                for index, task in enumerate(tasks, start=1):
                    print(f"{index:<6} | {task}")
                print("=" * 35)
                
                try:
                    task_num = int(input("\nEnter the number of the task to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed: '{removed}'")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == "4":
            print("\nGoodbye! Keep being productive.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    todo_app()1
    