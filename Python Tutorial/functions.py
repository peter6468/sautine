#function is a block of code wh/only runs when it is called
#in pyhton we dont use curly brackets, we use indentation w/tabs or spaces

#create function
def sayHello(name):
    #used an f string here
    print(f'Hello {name}')
#here we are calling thd funct
sayHello('John Doe')

def sayHello2(name="Sam"):
    #used an f string here
    print(f'Hello {name}')
#here we are calling thd funct
sayHello2()

#return values
def getSum(num1, num2):
    total = num1 + num2
    return total

#print(getSum(3,4)) 
# or
num = getSum(3,5)
print(num)

#lambda function is a small anonymous function
#lamda function can take any # of arguments, but can only have 1 expression
    #very similiar to JS arrow funct

#: is like arrow funct in js
getSum = lambda num1, num2: num1 + num2

print(getSum(10,3))

