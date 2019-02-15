# it/else conditions are used to decide to do something based on something
# being true or false
x = 21
y = 20

# comparison operators(==, !=, >, <, <=, >=) used to compare values
# change y= 50 will happen since its not true

# #simple if
# if x > y:
#     print(f'{x} is greater than {y}')

# # if/else
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# # elif
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{y} is greater than {x}')

# #nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')
#     #not a good way use logical operators instead

# # logical operators(and, or, not) - used to combine conditonal statements
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less tahn or equal to 10')
#     #way cleaner than above
# if x > 2 or x <= 10:
#     #or just one has to be true
#     print(f'{x} is greater than 2 or less tahn or equal to 10')

# if not (x == y):
#     print(f'{x} is not equal to {y}')

# membership operators(not, not in)
numbers = [1,2,3,4,5]
#in
# if x in numbers:
#     print(x in numbers)

# # #not in
# if x not in numbers:
#     print(x not in numbers)

#identity operators(is, is not)-compare objs, not if they are =, but if they
#are actually the same obj, with the same memory location
# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)


# -membership operators are used to test if a sequence is presented in an obj
