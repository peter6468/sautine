# class is like a blue print for creating objs.  obj has properties + methods(functs)
#ass w/it.  almost everything in python is an obj

#create class
class User:
    #constructor:basically a function tht runs when u instantiate an obj from a class
    #+ we want to def this as __
    def __init__(self, name, email, age):
        #self is this in js
        self.name = name
        self.email = email
        self.age = age

    #create method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    #another method
    def has_birthday(self):
        self.age += 1

#Extend class: class Customer extends: in pyhton we pass it in as a parameter
class Customer(User):
        #constructor:basically a function tht runs when u instantiate an obj from a class
    #+ we want to def this as __
    def __init__(self, name, email, age):
        #self is this in js
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#init user obj
brad = User("Brad Lim", "brad@gmail.com", 37)

#init customer obj
janet = Customer("Janet Jons", "janet@gmal.com", 69)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
#print(type(brad))
print(brad.greeting())

