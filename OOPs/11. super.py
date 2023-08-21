'''
If theres a parent class and a child class both __init__ function. Now if you instanciate a object with the child class but there are
some atrributes which u want to use from the parent class which is not defined in the child class eg in this code email....instead of 
having to add another parameter email in child class which created repetitive code we can just use super().__init__(attribute_name)

super() class basically refers to the class one above it....like here Wizard -> User -> object class so a super() being used in 
wizard class will refer to the one above parent class User.
'''


class User():
    def __init__(self, email):
        self.email = email
    
    def signed_in(self):
        print("User is logged in.")
        
    def attack(self):
        print("Do nothing.")
        
class Wizard(User):
    def __init__(self, name, power, email): #even User has a __init__ function...so to inherit the atrributes of parent class do as below
        self.name = name
        self.power = power
        super().__init__(email)     # same as using the below command, it does not take 'self' parameter
        # User.__init__(self, email)    
        #to avoid multiple same lines of self.email = email in child class as well we just inherited its property from parent class User in this class rather than defining it again
     
    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")

wizard1 = Wizard("John", 50, 'john@gmail.com')  #instanciated Wizard class....below 
print(wizard1.email)                            #wizard1.mail we are trying to get mail which is actually defined in User class                                            