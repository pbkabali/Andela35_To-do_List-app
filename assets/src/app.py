from tasks import todo_list, create_task, delete_task, mark_as_finished, delete_all_tasks
from accounts import accounts, add_account, login

if __name__ == "__main__":

    name = input("Enter your name: ")

    name = input("Please enter a password: ")

    if login(name,password)== True:
        return True
    else:
        add_account(name, password)

    print("Select Option:")
    print("1. Create Task")
    print("2. Mark Task as Finished")
    print("3. Delete Task")
    print("4. Delete all Tasks")
    print("Selection:")

    selection = input("Enter your selection")
    
    if selection == "1":
        task = input("Enter New Task")
        create_task(task)

    elif selection == "2":
        task = input("Enter Task to Mark as Finished")
        mark_as_finished(task)

    elif selection == "3":
        task = input("Enter Task to Delete")
        delete_task(task)

    elif selection == "4":
        delete_all_tasks
