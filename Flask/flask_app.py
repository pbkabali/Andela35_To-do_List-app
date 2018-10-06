from flask import Flask, request, render_template, url_for, jsonify
import json, registry, registered_users

app = Flask(__name__)

user=registry.User()

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


if __name__ == "__main__":
    app.run(debug=True)
