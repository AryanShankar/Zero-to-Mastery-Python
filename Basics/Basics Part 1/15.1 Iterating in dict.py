user = {
    "user": "Aryan",
    'age': 21,
    'result': True
}

for i in user: #prints the keys of the dictionary
    print(i)

print("\n")
for i in user.keys():
    print(i)

print("\n")
for i in user.values():
    print(i)

print("\n")
for i in user.items():
    keys, values = i
    print(keys,values) #returns seperate values
    print(i) #retuns a tuple

print("\n")
for key,value in user.items():
    print(key,value)