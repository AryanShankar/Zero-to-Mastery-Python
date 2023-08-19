li = ['a','b','c','d','e','d']
print(li.index('d')) # if that value is not there in the list, then it will throw an error and program will stop running.

# lookforelement:start:stop
print(li.index('d',0,5))

print('a' in li) # we use this to avoid the error.
print('x' in li)

name = 'saurabh'
print('b' in name) # we can use this with strings as well

print(li.count('d')) #number of occurences of element in list

#all these return some value but dont modify the list in anyways