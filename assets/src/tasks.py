todo_list = []

def create_task(task):
    todo_list.append(task)
    print("Your current List is shown below:")
    for i in todo_list:
       print (str(todo_list.index(i)+1)+". " + i)
    additional_task = input("Press 1 to add another Task, Press any key if you are done:")
    if additional_task == "1":
        task_to_add = input("Add another Task:")
        create_task(task_to_add)
    else:
        print("your tasks have been recorded")

def delete_task(task):
    print("Are you sure you want to delete"+" "+ task.upper() +"? Y/N:")
    delete_confirmation = input()
    if delete_confirmation == "Y" or delete_confirmation == "y":
        todo_list.remove(task)
        print("Your current List is shown below:")
        for i in todo_list:
            print (str(todo_list.index(i)+1)+". " + i)
        other =input("Press 1 to delete another task, Press any key if you are done:")
        if other == "1":
            new_delete_index=input("Enter the number for item to delete:")
            delete_task(todo_list[int(new_delete_index)-1])
        else:
            print("Your tasks have been deleted")
    elif delete_confirmation == "N" or delete_confirmation == "n":
        print("Returning to main menu......")
    else:
        print("Invalid response!")
        print("Returning to main menu......")




def mark_as_finished(task):
    todo_list[todo_list.index(task)] = task + '[FINISHED]'
    print("Your current List is shown below:")
    for i in todo_list:
        print (str(todo_list.index(i)+1)+". " + i)
    other =input("Press 1 to mark another task, Press any key if you are done:")
    if other == "1":
        new_mark_index=input("Enter the number for item to mark:")
        mark_as_finished(todo_list[int(new_mark_index)-1])
    else:
        print("Your finished tasks successfully marked")


def delete_all_tasks():
    todo_list.clear()
    print("Your current list is now empty:")
    