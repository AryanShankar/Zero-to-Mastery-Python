#Unordered thus no index only key based, Mutable

my_dict = {
    'a' : [1,2,3],
    'b' : "hello",
    'c' : True
    }

my_list = [
    {
    'a' : [1,2,3],
    'b' : "hello",
    'c' : True
    },
    {
    'a' : [4,5,6],
    'b' : "bye",
    'c' : False
    }
    ]

print(my_dict["a"])
print(my_dict["a"][1])
print(my_list[1]["a"][2])




#Keys needs to be immutable thus lists cant be used as keys 
#tuples can be used as keys

print("\nPart-2")
my_dict = {
    123 : [1,2,3],
    'cac' : "hello",
    False : True,
    123 : "hahaha" #if 2 keys of same name present, it will overwrite the previous key value...so now 123 key will have hahaha 
    }

print(my_dict[False])
print(my_dict[123]) #overwrites 