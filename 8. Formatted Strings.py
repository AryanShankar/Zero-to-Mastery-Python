#Printing 
a,b,c = 1,2,3
a = "john"


print("hi " + a + " your age is= ", b)
print("hi ", a , " your age is= ", b) #  , gives space kudh sey ek aage ya piche

print("hi "+ a + " your age is=", b)
    
print("hi "+ a , " your age is= ", b)




print(f"Hi {a} my age is {c}")
print("hi {1} my age is {0} and number {f} is cool".format(a,b,f=7))


#Formatted Strings

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))


name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")

