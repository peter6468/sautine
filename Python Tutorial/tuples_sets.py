#tuple is a collection wh/is ordered and unchangeable, allows dup members

#create tuple: use()
fruits = ("Apples", "Orange", "Grapes")
#fruits2 = tuple(("Apples", "Orange", "Grapes"))

#single val needs trailing comma or it comp will thinks its a str
fruits2 =("Apples",)

print(fruits, fruits2)

print(fruits2, type(fruits2))

#w/tuples if u only have 1 value, u want to leave a trailing comma

#cant change value
#frutis[0] = "Pears"

del fruits2

#get length
print(len(fruits))

# a set is collection wh/is unordred and unindexed, no dup members

#create set use curly brackets
fruits_set = {"Apples", "Oranges", "Mango"}

#check if in set
print("Apples" in fruits_set)

#add to set
fruits_set.add("Grape")
print(fruits_set)

#remove from set
fruits_set.remove("Grape")
print(fruits_set)

#clear set
fruits_set.clear()
print(fruits_set)

## delete
#del fruits_set and print will get undefined error

## if u add duplicate, it will no show up 2x