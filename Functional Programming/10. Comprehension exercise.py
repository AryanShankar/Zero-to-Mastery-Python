'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

Convert this code into comprehension
'''

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({i for i in some_list if some_list.count(i) > 1})  #curly brackets to do set comprehension to avoid duplicates and then do list to convert the list to list
#duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))   list comprehension /ZTM solution 

print(duplicates)