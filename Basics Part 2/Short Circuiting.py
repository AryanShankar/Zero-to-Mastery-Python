x = True
b = False

if x and b: #now in this if x is false compiler short circuits its execution and does not check for b as it can be heavy operation
    print(True)
if x or b: #now in this if x is true then again same compiler will short circuit the execution for checking the other condition b
    print(True)