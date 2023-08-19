print(True == 1) #true
print(True == 50) #false
print('' == 1) #false
print(' ' == 1) #false
print('A' == 65) #false
print([] == 1) #false
print(10 == 10.0) #true
print([] == []) #true
print('1' == 1) #false

print(chr(65))
print(ord('A'))

print(bool(50)) #true
print(bool('1')) #true

print("\nPart 2\n")

print(10 is 10) #true
print(True is True) #true
print(True is 1) #false
print('' is 1) #false
print(' ' is 1) #false
print('A' is 65) #false
print([] is 1) #false
print(10 is 10.0) #false
print('1' is 1) #false
print([] is []) #false
print([1,2,3] is [1,2,3]) #false, tho lists are same they r stored in different locations thus gives o/p as false

#== checks for value being same while is checks for location needing to be same and exact same value