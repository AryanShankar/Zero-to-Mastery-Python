#mutable, ordered

li = [1, 2.5, "hello", True]
print(li)

amazon_cart = [
    "laptop",
    "book",
    "phone",
    "pen",
    "key"
   ]

#LIST SLICING:
# start:stop:stepover
print(amazon_cart[0])
print(amazon_cart[::-1])
print(amazon_cart[0:2])
print(amazon_cart)

print("\nPart-2")
new_cart = amazon_cart # here we are actually passing the address of the old list, 
                       # and not copying and storing the list in new location.
new_cart[0] = "PC" # lists are mutable, unlike strings which are immutable.
amazon_cart[2] = 'idk'
print(amazon_cart) # notice that the old list is also modified.
print(new_cart)

print("\nPart-3")
flipkart_cart = amazon_cart[:] # here we are actually copying the whole list to another location or we can use .copy()
flipkart_cart[0] = "headphones"
print(amazon_cart) #thus old list remains unchanged this time
print(flipkart_cart)

print("\nPart-4")
my_list = [1,2,3]
bonus = my_list + [5] #its copying list into new list
my_list[0] = 'z'
bonus[1] = '8'
print(my_list)
print(bonus)

print("\nPart-5")
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:6]) #will print b c
#new_list[6] will give IndexError: list index out of range

print("\nPart-6")
print(list(range(101)))