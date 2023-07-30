#some list methods will modify original list and not return any value, some may modify and return some value, some will return value and not modify original list

#ADDING
print("\nappend")
li = [1,2,3,4,5]
new_li = li.append(100) #as method doesnt return anything value of new_li is None, only original string is modified
print(li)
print(new_li)

print("\ninsert")
new_li = li.insert(2,2000) #(index, value)
print(li)
print(new_li)

print("\nextend")
new_li = li.extend([45,"hello"])
print(li)
print(new_li)



#DELETING:
print("\npop")
new_li = li.pop() #returns the value removed from the list and modifies the original list
print(li)
print(new_li)

print("\npop")
new_li = li.pop(0) # (index)
print(li)
print(new_li)

print("\nremove")
new_li = li.remove(2000) #(value)
print(li)
print(new_li)

print("\nclear")
new_li = li.clear()
print(li)
print(new_li)