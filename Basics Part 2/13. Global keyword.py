total = 0

def count():
    # global total total += 1    this gives error first declare total as global then perform operations like done below
    global total 
    total += 1  # here we are referenced total before assignment, hence we have declare 'global total' first 
    return total

count()
count()
count()

print(total)

#better way to do this will be to pass total value as parameter:
#print(count(count(count(total))))

# i += 1 	# this gives error, similaryly we have declare total first in the count() function