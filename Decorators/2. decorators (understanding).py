def my_decorator(func):
    def wrap_func():
        print("***********")
        func()
        print("***********")
    print(wrap_func)
    return wrap_func

@my_decorator
def hello():
    print("Hello!")

hello()

# using decorator is same as doing the below:
# my_decorator(hello)()


print("\npart2\n")
def hi():
    print("Hello!")

#we can also write mydecorator(hi)() directly      so the wrap_func() returned is also ran becoz of the ()
hi2 = my_decorator(hi) #returns wrap_func in hi2
hi2() #same as the wrap_func (see same location)
print(hi2)

