from tasks import todo_list, create_task, delete_task, mark_as_finished, delete_all_tasks
from accounts import accounts, add_account, login

if __name__ == "__main__":

    print ("Welcome to Polos To-do List app!")
        
    name = input("Enter your username:")

    password = input("Please enter a password: ")

    if login(name,password):
        print("Successfully Logged in")      
        print("Please select one of the options below:")
        print("1. Create Task")
        print("2. Mark Task as Finished")
        print("3. Delete Task")
        print("4. Delete all Tasks")
#       print("5. Sign-out and exit app")
        
        selection = input("Enter your selection:")

        if selection == "1":
            new_task= input("Add task:")
            create_task(new_task)

        elif selection == "3":
            for i in todo_list:
                print(str(todo_list.index(i)+1)+". " + i)
            delete_index=input("Enter the number for item to delete:")
            delete_task(todo_list[int(delete_index)-1])
        
        elif selection == "2":
            for i in todo_list:
                print(str(todo_list.index(i)+1)+". " + i)
            mark_index=input("Enter the number for item to mark:")
            mark_as_finished(todo_list[int(delete_index)-1])
        
        elif selection == "4":
            delete_all_tasks()          
            

        
    else:
        print ("Non-existent account!")
        
        add_account(name, password)
        print ("Created account with entered details")

        print("1. Create Task")
        print("2. Mark Task as Finished")
        print("3. Delete Task")
        print("4. Delete all Tasks")
#       print("5. Sign-out and exit app")
        
        selection = input("Enter your selection:")

        if selection == "1":
            new_task= input("Add task")
            create_task(new_task)

        elif selection == "3":
            for i in todo_list:
                print(str(todo_list.index(i)+1)+". " + i)
            delete_index=input("Enter the number for item to delete:")
            delete_task(todo_list[int(delete_index)-1])
        
        elif selection == "2":
            for i in todo_list:
                print(str(todo_list.index(i)+1)+". " + i)
            mark_index=input("Enter the number for item to mark:")
            mark_as_finished(todo_list[int(delete_index)-1])
        
        elif selection == "4":
            delete_all_tasks()          


        