my_list = []

for item in 'hello':
    my_list.append(item)

print(my_list)

my_list1 = [item for item in 'hellooh']
print(my_list1)

my_list2 = [num**2 for num in range(1,11)]
print(my_list2)

my_list3 = [num*2 for num in range(1,11) if num % 2 == 0] #use square brackets for list comphrehension
print(my_list3)

print("\n")
# printing only even squares
my_set = {num**2 for num in range(1,11) if num**2 % 2 == 0} #use curly brackets for set comphrehension
print(my_set)

my_set2 = {item for item in 'hellooh'}
print(my_set2)
# remember that set don't contain duplicate values