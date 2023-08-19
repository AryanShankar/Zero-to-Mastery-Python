li = ['a','b','c','d','e','z','d']

#this modifies the original list but does not have any return value thus print result is None
print(li.append('5'))
print(li.remove('e'))
#print(li.sort()) #returns None but modfies the list to sorted elements


#these only return a particular value but does not modify the list
print(li.pop())
print(li.index('c'))
print(li.count("d"))
print(sorted(li)) #prints the sorted list without modifying the list 

print(li[::-1])

#modifies original list and returns a value of what element was popped off 
print(li.pop(3)) 


