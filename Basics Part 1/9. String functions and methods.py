quote = "to Be be or nOt to be"

print(len(quote)) #bulit in function


#functions/built in fucntions are with only brackets eg. len(quote)
#methods are with dots eg. quote.format() 
print(quote.upper())

quote.lower() #methods does not alters the value of strings because strings are immutable 
print(quote) #All string methods returns new values. They do not change the original string.

print(quote.replace('be', 'me')) 
print(quote)

print("\nPART 2\n")

quote = "to be or not to be"
print(quote.capitalize())
print(quote)    # notice that the original message is unchanged, becuase strings are immutable
quote = quote.capitalize()
print(quote)
print(len(quote)) # len() is a function and not a string method
print(quote.upper())
print(quote.find("not"))
print(quote.replace("be","me"))



