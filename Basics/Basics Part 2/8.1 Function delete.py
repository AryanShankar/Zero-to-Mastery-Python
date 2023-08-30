
def hello():
    print("hello!")
    
greet = hello

greet()
print(hello)
hello()

del hello   #it deletes the word hello referencing to the function but greet still works 
# here the function is not deleted, just the keyword, because greet is still pointing to the function memory
# and python has not deleted it
#(hello()  # this will give error, because it has been deleted
print(greet)
greet()
