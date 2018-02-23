data = [1,2,3,5,8]

# Receive string input from standart input cmd
input = input()

# Convert string to int
search_for = int(input)

# Search for input provided by user
for x in data:
    if x == search_for:
        print("search data found = {}".format(x))
        break
