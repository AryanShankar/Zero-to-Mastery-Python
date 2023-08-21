class SuperList(list):
   def __len__(self):
      return 1000
     
super_list1 = SuperList()
print(super_list1) #this usually wud return the address of object but here as the class has inherited from list class it retuns the value of the list

super_list1.append(5)
super_list1.append(0)
super_list1.append(100)
print(super_list1)
print(super_list1[0])

print(len(super_list1))

print(issubclass(SuperList, list))
print(issubclass(list, object))