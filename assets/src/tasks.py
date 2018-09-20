todo_list = []

def create_task(task):
    todo_list.append(task)
    print("Your current List is shown below:")
    for i in todo_list:
       print (str(todo_list.index(i)+1)+". " + i)
    additional_task = input("Enter 1: to add another Task, Press any key To finish adding Tasks")
    if additional_task == "1":
        task_to_add = input("Add another Task")
        create_task(task_to_add)

def delete_task(task):
    todo_list.remove(task)
    print("Your current List is shown below:")
    for i in todo_list:
        print (str(todo_list.index(i)+1)+". " + i)
    other =input("Press 1 to delete another task, Press any key if you are done")
    if other == "1":
        new_delete_index=input("Enter the number for item to delete")
        delete_task(todo_list[int(new_delete_index)-1])



def mark_as_finished(task):
    todo_list[todo_list.index(task)] = task + '[FINISHED]'
    print("Your current List is shown below:")
    for i in todo_list:
        print (str(todo_list.index(i)+1)+". " + i)
    other =input("Press 1 to mark another task, Press any key if you are done")
    if other == "1":
        new_mark_index=input("Enter the number for item to mark")
        mark_as_finished(todo_list[int(new_mark_index)-1])


def delete_all_tasks():
    todo_list.clear()
    print("Your current List is shown below:")
    for i in todo_list:
        print (str(todo_list.index(i)+1)+". " + i)
