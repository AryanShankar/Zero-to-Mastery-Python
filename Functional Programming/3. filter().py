#in map() we always get the same number of items back that were given in input. We just map over each item.
#filter() removes or filter out some of the input based on the condition provided.

def only_even(item):
    return item % 2 == 0

my_list = [5,8,9,2,5,6,98,56,62]

print(filter(only_even, my_list))  
print(list(filter(only_even, my_list))) 

print(map(only_even, my_list))
print(list(map(only_even, my_list))) 

print(my_list)