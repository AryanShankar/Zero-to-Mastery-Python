class PlayerCharacter:
    membership = True   # Class object attribute, its an attribute of PlayerCharacter. It is a static attribute and true for all objects created
    def __init__(self, name, age):
        if self.membership :    # or we can write: 'if PlayerCharacter.membership :'
            self.name = name  # these are dynamic attribute and different for different objects unlike class object attributes
            self.age = age
            
    def run(self):
        print(f"run {self.name}")
        # print(f"run {PlayerCharacter.name})   # we cannot do this because name is defined in the constructor and is dynamic and not a static class object attribute

player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 98)

print(player1.name)
print(player1.membership)   # each of the class instace(objects) can assess the class object attribute
print(player1.run())