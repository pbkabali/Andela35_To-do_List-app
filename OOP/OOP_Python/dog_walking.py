
class Pets:

    def __init__(self, list_of_pets, type_of_pets, class_of_pets):
        self.list_of_pets = list_of_pets        
        self.type_of_pets = type_of_pets
        self.class_of_pets = class_of_pets
        
    def pets_report(self):
        print ("I have " + str(len(self.list_of_pets))+" "+ self.type_of_pets +".") 
        for i in self.list_of_pets:
            i.report_age()
        print ("And they're all "+ self.class_of_pets +", of course.")
        hungry = []
        for i in self.list_of_pets:
            hungry.append(i.eat())
        if all(x==True for x in hungry):
            print("My dogs are hungry.")
        elif all(x==False for x in hungry):
            print("My dogs are not hungry.")
        else:
            print("Some of my dogs are hungry")

    def walk(self):
        for i in self.list_of_pets:
            print(i.name + " is walking!.")




class Dog:
    def __init__(self,name,age,hours_since_last_meal):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.hours_since_last_meal = hours_since_last_meal

    def report_age(self):
        print (self.name + " is "+ str(self.age)+".")

    def eat(self):
        if self.hours_since_last_meal <= 5:
            self.is_hungry = False
        return self.is_hungry
    
    def walk(self):
        print(self.name + " is walking!.")


dog1=Dog("Tom",6,4)
dog2=Dog("Fletcher",7,3)
dog3=Dog("Larry",9,2)
my_pets = Pets([dog1,dog2,dog3], "dogs", "mammals")
my_pets.walk()

