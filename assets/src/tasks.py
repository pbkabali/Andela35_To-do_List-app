todo_list = []

def create_task(task):
    todo_list.append(task)

def delete_task(task):
    todo_list.remove(task)

def mark_as_finished(task):
    todo_list[todo_list.index(task)] = task + '[FINISHED]'

def delete_all_tasks():
    todo_list.clear()
