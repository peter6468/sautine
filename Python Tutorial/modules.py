# module is basically a file containing a set of functs to include in your application
#there are core python modules, modules u can install using the pip package manger
#(including Django) as well as custom modules

#core modules
import datetime
from datetime import date
import time
from time import time

#pip module
from camelcase import CamelCase

#import custom module
import validator
from validator import validate_email
#today = datetime.date.today()
today = date.today()
#timestamp = time.time()
timestamp = time()

c= CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')


print(today)
print(timestamp)

#python has package manager called pip comapring it to js where you have node.js and 
#your npm package mamager

# using pip3 instead of pipenv
# virtual env w/pip it gets just gets installed in that env