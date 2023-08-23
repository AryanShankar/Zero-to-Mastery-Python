#squre each value of list and print
print(list(map(lambda num: num**2, [1,2,3])))


#sort using second index of the tuple in the list
a = [(0,2),(4,4),(10,-1),(5,3)]

a.sort(key=lambda x:x[1], reverse=False)
print(a)

'''
The sort() method accepts a reverse parameter as an optional argument. Setting reverse = True sorts the list in the descending order.
'''