#list is a collection wh/is ordered and chageable.  allows duplicate members like ARRAYS in JS

#create list
numbers = [1,2,3,4,5]
fruits = ["Apples", "Ornages", "Grapes", "Pears"]

#use a constrctor
#numbers2 = list((1,2,3,4,5))

#print(numbers, numbers2)


print(fruits[1])

#get length
print(len(fruits))

#append to list
fruits.append("Mango")
print(fruits)

#remove from list
fruits.remove("Grapes")
print(fruits)

#insert into position
fruits.insert(2, "Strawberries")
print(fruits)

#remove w/pop
fruits.pop(2)
print(fruits)

#reverse list
fruits.reverse()
print(fruits)

#sort list
fruits.sort()
print(fruits)

#reverse sort
fruits.sort(reverse=True)
print(fruits)

#change value
fruits[0] ="Blueberries"
print(fruits)