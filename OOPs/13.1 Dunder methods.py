
class ActionFig():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {"name": "yoyo", "has_pets": "Dog"}
    
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__(self):
        return 'hello...??'
    
    def __getitem__(self, i):
        return self.my_dict[i]
    
    def __del__(self):
        return 'deleted'
    
hulk = ActionFig("red", 0)

#if we try to use str or __str__() aise it will return the location of an object (actually its used for turning variables into strings but for objects if u write str(object_name_forclass) it returns address of object like print(object_name))
print(hulk.__str__())
print(hulk)
print(str(hulk))
print(str('Printing an string')) #outside class

print(hulk.__len__())
print(len(hulk))
print(len('0123456789')) #outside class

print(hulk.__call__())
print(hulk())   # with call method, we get this special power to call a method with curly braces

print(hulk.__getitem__("has_pets"))

print(hulk.__repr__()) # it is same as print(hulk), it prints the memory location of the object

print(hulk.__del__())
del hulk    # this deletes the variable passed, but as we have modified it, it won't delete the instance now

a = 5
del a
# print(a)  
'''
this will give us error, because we have deleted the variable a, 
because we haven't modified the base class __del__ method, so its performing normal
'''