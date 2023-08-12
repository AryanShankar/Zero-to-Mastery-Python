# we can pass any iterable to enumerate, and it will store them as separate tuple with index starting from 0.
for i in enumerate('Hello World'):
    print(i)

print("\n")
for i,char in enumerate(list(range(10))):
    if i == 5:
        print(f"index of 5 is {i}")

print("\n")
for i,j in enumerate([1,2,3,4]):
    print(i,j)

print("\n")
for i,j in list(enumerate([1,2,3,4])):
    print(i,j)

print("\n")
for i in enumerate((1,2,3,4,5)):
    print(i)

print("\n")
print(list(item for item in enumerate('123456789')))
print((i * i for i in range(8)))

print(list(enumerate('123456789')))

print(dict(list(enumerate((i * i for i in range(1,11)),1)))) #doubt