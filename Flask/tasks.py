todo_list = []
deleted_items = []

class task_operation:

    def create_task(self, task):
        todo_list.append(task)
        
    def view_list(self):
        ordered_list = {}
        for item in todo_list:
            ordered_list[todo_list.index(item)+1] = item
        return ordered_list
        
    def delete_task(self, task):
        if task in todo_list:
            todo_list.remove(task)
            deleted_items.append(task)
            return True
        else:
            return False
    
    def mark_as_finished(self, task):
        todo_list[todo_list.index(task)] = task + '[FINISHED]'

    def unmark_as_finished(self, task):
        unmarked_task = ''
        for i in range (len(task)-len('[FINISHED]')):
            unmarked_task += task[i]
        todo_list[todo_list.index(task)] = unmarked_task

    def delete_all_tasks(self):
        for task in todo_list:
            deleted_items.append(task)
        todo_list.clear()

    def view_deleted_items(self):
        deleted_tasks = {}
        for item in deleted_items:
            deleted_tasks[deleted_items.index(item)+1] = item
        return deleted_tasks
       
    def recover_deleted_task(self, task):
        todo_list.append(task)
        deleted_items.remove(task)
    