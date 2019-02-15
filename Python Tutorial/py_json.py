#json is commonly used w/data apis.  here we can parse json into a python dictionary

import json

#smaple json
userJSON = '{"first_name": "Dick", "last_name": "Gazinya", "age": 30}'

#parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

#take dict and make into json
car = {'make': 'Ford', 'nodel': 'Mustang', 'year': 1970}

carJSON =json.dumps(car)

print(carJSON)