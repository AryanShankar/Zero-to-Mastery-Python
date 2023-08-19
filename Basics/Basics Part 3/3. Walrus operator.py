a = 'helloooooooooo'

if ((n := len(a)) > 10): #basically it does n = len(a) 
    print(f"too long {n} elements")
print(n)

print("\n")
while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)