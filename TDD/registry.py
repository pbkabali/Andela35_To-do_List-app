from registered_users import user_accounts
import re
class User:

    def __init__(self):
        self.status = "inactive"
        self.details = {}
        self.username= "unknown"
    
    def register(self, name, username, password, age, email, gender): 
        #check that username is not same as name or less than 4 characters
        if username.upper() in name.upper():#changing case will not make same username acceptable
            raise ValueError("username cannot be one of your names")
        elif len(username) < 4:
            raise ValueError("username must be atleast 4 characters long") 
        else:
            user_accounts[username]={}

        user_accounts[username]["Name"] = name
        user_accounts[username]["Password"] = password
        
        #check for correct email format
        match = re.match(r'^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match == None:
	        raise ValueError('Bad email address format')
        else:
            user_accounts[username]["Email"] = email
        
        #check that age entered in a number and is non-negative
        if type(age) == str:
            raise ValueError("Age must be a number")
        elif age < 0:
            raise ValueError("Age must be non-negative")   
        
        else:    
            user_accounts[username]["Age"] = age
        
        user_accounts[username]["Gender"] = gender
       

    def login(self, username, password):
    
        if username in user_accounts and user_accounts[username]["Password"] == password:
            self.status = "active"
            self.username = username
            self.details = user_accounts[username]
            status = "Successfully logged in"
        else:
            status = "Wrong details entered!"
        return status  

    def view_user_details(self):

        if self.status == "active":
            return {
                "Name":self.details["Name"]
                ,"Age":self.details["Age"]
                ,"Email":self.details["Email"]
                ,"Gender":self.details["Gender"]
            }

        else:
            print ("You have to be logged in to see account details!") 

    def view_email(self):
        if self.status == "active":
            print (self.details["Email"])
        else:
            print ("You have to be logged in to see account details!") 

    def view_age(self):
        if self.status == "active":
            print (self.details["Age"])
        else:
            print ("You have to be logged in to see account details!") 
    
    def view_gender(self):
        if self.status == "active":
            print (self.details["Gender"])
        else:
            print ("You have to be logged in to see account details!") 

    def change_username(self, old_password,new_username):
        if self.status == "active":
            confirmation = old_password
            if self.details["Password"] == confirmation:
                user_accounts[new_username] = self.details
                del(user_accounts[self.username])
                self.username = new_username
                return "Your username has been changed to: " + new_username

            else:
                return "You have supplied an incorrect confirmation password!"          

        else:
            return "You have to be logged in to change account details!" 
    
    def change_email(self, old_password, new_email):
        if self.status == "active":
            confirmation = old_password
            if self.details["Password"] == confirmation:
                user_accounts[self.username]["Email"] = new_email
                return "Your email has been changed to: " + new_email

            else:
                return "You have supplied an incorrect confirmation password"                

        else:
            return "You have to be logged in to change account details!"  

    def change_password(self,old_password, new_password):
        if self.status == "active":
            confirmation = old_password
            if self.details["Password"] == confirmation:
                user_accounts[self.username]["Password"] = new_password
                return "Your password has been successfully changed."
            else:
                return "You have supplied an incorrect confirmation password"                

        else:
            return "You have to be logged in to change account details!"  

   

if __name__=="__main__":

    user1 = User()

    user1.register("paul balitema", "pbk", "kabali", 30, "engineerbpk@gmail.com", "male")

    print (user_accounts)
   
    