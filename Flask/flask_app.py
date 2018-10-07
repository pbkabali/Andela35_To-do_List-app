from flask import Flask, request, render_template, url_for, jsonify
import json, registry, registered_users, tasks

app = Flask(__name__)

user = registry.User()
operation = tasks.task_operation()

@app.route('/')
def home_page():
    return "Welcome to Polos Todo list app!"

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        age = int(request.form.get('age'))
        email = request.form.get('email')
        gender = request.form.get('gender')
        user.register(name, username, password, age, email, gender)
        return 'Your account has been created!'

@app.route('/users')
def view_users():
    return jsonify(registered_users.user_accounts)

@app.route('/users/login', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if user.login(username,password):
        return "You are successfully logged in"
    else:
        return "Your details did not match!"        

@app.route('/users/logout')
def logout():    
    user.logout()
    return 'Successfully logged out!'

@app.route('/users/delete', methods = ['DELETE'])
def delete_user():
    if user.delete_user():
        return 'user successfully deleted!'
    else:
        return "Not logged in!"

@app.route('/tasks')
def view_list():
    return jsonify(operation.view_list())

@app.route('/tasks/addtask', methods = ['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_to_add = request.form.get('task')
        operation.create_task(task_to_add)
        return  jsonify(operation.view_list())

@app.route('/tasks/delete', methods =['POST'])
def delete_task():
    task_to_delete = request.form.get('task')
    if not operation.delete_task(task_to_delete):#confirm if task to delete is in list
        return 'Task not found!'
    else:
        operation.delete_task(task_to_delete)
        return  jsonify(operation.view_list())

@app.route('/tasks/deleteall', methods = ['DELETE'])
def delete_all_tasks():
    operation.delete_all_tasks()
    return 'Your todo list is now empty!'

@app.route('/tasks/undelete', methods = ['GET', 'POST'])
def recover_task():
    if request.method == 'POST':
        task_to_recover = request.form.get('task')
        operation.recover_deleted_task(task_to_recover)
        return jsonify(operation.view_list())

    return jsonify(operation.view_deleted_items())

@app.route('/tasks/mark', methods = ['POST'])
def mark_task():
    task_to_mark = request.form.get('task')
    operation.mark_as_finished(task_to_mark)
    return jsonify(operation.view_list())


@app.route('/tasks/unmark', methods = ['POST'])
def unmark_task():
    task_to_unmark = request.form.get('task')
    operation.unmark_as_finished(task_to_unmark)
    return jsonify(operation.view_list())        
    



if __name__ == "__main__":
    app.run(debug=True)
