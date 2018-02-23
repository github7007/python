courses = {
            "AWS":15000,
            "Python":10000,
            "DevOps":15000,
            "Java":12000
          }

# Modifying dictionary
courses['DevOps'] = 20000

# Adding new entry to the dictionary
courses['Data Science'] = 20000

# Accessing keys in dictionary
print(courses['AWS'])
print(courses['DevOps'])

# Accessing keys in loop
for c in courses:
    print(c)

# Accessing values in loop
for c in courses:
    print(courses[c])

# Accessing keys/values in loop
for c in courses:
    print("{}, fee is {}".format(c,courses[c]))
