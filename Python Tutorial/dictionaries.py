#dictionary is a collection wh/is unordered, changeable and indexed. No dupilicate members
# very similiar ot object literal in js

# Create dict
person = {
    "first_name": "Peter",
    "last_name": "Lim",
    "age": 48
}

# #use constructor
# person2 = dict(first_name="Sara", last_name="Williams")
# print(person, type(person))
# print(person2, type(person2))

#GET VALUE
#   in js print(person.name) w/obj literal
print(person["first_name"])
print(person.get("last_name"))

#add key/value
person["phone"] = "555-555-5555"

#get dict keys + ote,s
print(person.keys())
print(person.items())

#copy doct
#similiar to spread operator in js
person2 = person.copy()
person2["city"] = "Boston"

print(person2)
#remoive an item
del(person["age"])
person.pop("phone")

#clear

print(person)
#will get empty dict {}

#get length
print(len(person2))

#list of dict
people = [
    {
        "name": "Ben",
        "age": 30
    },
    {
        "name": "Ralph",
        "age": 34
    }
]

print(people)
print(people[1]["name"])