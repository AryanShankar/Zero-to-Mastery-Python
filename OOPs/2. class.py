'''
Note: Self refers to the object itself. So, self.name is nothing but player1.name
this way by using self, we pass the object itself to the class.
Every class method should have first argument as 'self'
and first method should be __init__ method.
'''

class PlayerCharacter:
    def __init__(self, name, age): #this is a constructor and it gets called everytime we instantiate a object
        self.name = name    # Attribute or Property
        self.age = age
        print("I get printed at every instance created")
        
    def run(self):
        print("run method")
        # return "Done"

player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 98)
player2.attack = True   # creating a new attribute for the player2

print(player1)  # Memory location of the object
print(player1.name)  # Notice that we are accessing the attributes, and hence we are not using the curly brackets at the end
print(player1.age)

print(player2)
print(player2.name)
print(player2.age)

print(player1.run())    # Here we are accessing the method, and hence using curly brackets
#the method returns nothing hence None is printed by this print function

print(player2.attack)

