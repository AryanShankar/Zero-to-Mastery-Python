# *args and **kwargs

def super_func(*args, **kwargs):    # we can actually name these parameters anything we want, 
                                    # but its a good practice to give the same name only.
    print(args) #grabs any number of positional arguments and stores them in a tuple
    print(type(args)) 	# class tuple
    print(*args)
    # print(type(*args)) 	# gives error
    # print(sum(*args))     # gives error as sum() can take only one parameter and *args is 1 2 3 4 5
    print(sum(args))

    print(kwargs) #grabs any number of keyword arguments and puts them in a dict
    # print(**kwargs) 	# gives error
    print(kwargs.keys())
    print(kwargs.values())
    print(type(kwargs)) 	# class dict

    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))


# Rules for the order of parameters:
# positional parameters, *args, default parameters, **kwargs
# for eg.
# def super_func2(name, *args, age = 10, **kwargs):