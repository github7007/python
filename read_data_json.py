import json

# open() is built in function to read/write data to file
file_data = open('data.json').read()

# json.loads reads data from file and converts into object
data = json.loads(file_data)
name = data['name']
age = data['age']
company_name = data['company']['name']
location = data['company']['location']

print("Name = {} ".format(name))
print("Age = {} ".format(age))
print("Company name = {} ".format(company_name))
print("Company Location  = {} ".format(location))
