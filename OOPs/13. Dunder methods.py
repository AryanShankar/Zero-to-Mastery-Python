#dunder methods are all inherited from the object class
#we can do basic customizations or modify the dunder methods according to our needs for a particular class

class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      print(i)
      return self.my_dict[i]


action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))
print(action_figure.__len__())

print(action_figure()) #call the function

print(action_figure['name'])

del action_figure