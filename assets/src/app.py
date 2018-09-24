from tasks import todo_list, create_task, delete_task, mark_as_finished, delete_all_tasks
from accounts import accounts, add_account, login

if __name__ == "__main__":

    print ("WELCOME TO POLOS TO-DO LIST APP!")
        
    name = input("To use the app, enter your username:\n")

    password = input("Please enter your password: \n")

    def menu():
        print ("**************************************")
        print("PLEASE SELECT ONE OF THE OPTIONS BELOW:")
        print("1. Create Task")
        print("2. Mark Task as Finished")
        print("3. View your to-do list")
        print("4. Delete Task")
        print("5. Delete all Tasks")
        print("0. Sign-out and exit app")
        print ("**************************************")

    def task_operations():
        selection = input()

        if int(selection) not in range(6):
            print("Unavailable option!")
            menu()
            task_operations()

        elif len(todo_list) == 0 and int(selection) in range(2,6):
            print("Your To-do list is empty")
            menu()
            task_operations()

        else:
            if selection == "1":
                new_task= input("Add task:")
                create_task(new_task)
                menu()
                task_operations()

            elif selection == "3":
                print("Your current List is shown below:")
                for i in todo_list:
                    print(str(todo_list.index(i)+1)+". " + i)
                menu()
                task_operations()

            elif selection == "4":
                for i in todo_list:
                    print(str(todo_list.index(i)+1)+". " + i)
                delete_index=input("Enter the number for item to delete:")
                if int(delete_index) in range(len(todo_list)+1):
                    delete_task(todo_list[int(delete_index)-1])
                    menu()
                    task_operations()
                else:
                    print("item not found on list")
                    menu()
                    task_operations()
            
            elif selection == "2":
                for i in todo_list:
                    print(str(todo_list.index(i)+1)+". " + i)
                mark_index=input("Enter the number for item to mark:")
                mark_as_finished(todo_list[int(mark_index)-1])
                menu()
                task_operations()
            
            elif selection == "5":
                print("Are you sure you want to delete all your tasks? Y/N:")
                delete_all = input()
                if delete_all == "Y" or delete_all == "y":
                    delete_all_tasks()
                    menu()
                    task_operations()
                elif delete_all == "N" or delete_all == "n":
                    menu()
                    task_operations()
                else:
                    print("Invalid Response")
                    menu()
                    task_operations()

            elif selection == "0":
                print("!!!THANKS FOR USING OUR APP!!!")


    if login(name,password):
            print("Successfully Logged in")      
            menu()
            task_operations()    
        
    else:
        print ("Non-existent account or wrong login details")

        print("Press 1 to enter your details again:")
        print("Press 0 to create new account with username:"+" "+name)
        new_account = input()

        if new_account == "1":
            name = input("To use the app,enter your username:\n")
            password = input("Please enter your password: \n")
            if login(name,password):
                print("Successfully Logged in")      
                menu()
                task_operations()
                 
        elif new_account == "0":
            password = input("Please create password: \n")         
            add_account(name, password)
            menu()
            task_operations()

        

       
        