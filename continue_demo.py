data = [1,2,0,4,0,5]

result = 1

# Skip the logix when value in array is zero

for x in data:
    if x == 0:
        continue
    result = result*x

print("Result = {}".format(result))
