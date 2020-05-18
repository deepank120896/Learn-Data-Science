## Strings

text = 'Hi I am Deepank'
print(text[1]) # specific character 
print(len(text)) # length of string
print()

# string slicing
print("... SLICING ...")
s = text[1:8] # slice string from index 1 upto 7
print(s)
s = text[0:] # slice from 0 upto last index
print(s)
s = text[:5] # slice string from 0 upto 4
print(s)
print()

# string in-built functions
print("... STRING METHODS ...")
a = "Hi Hi Hello Bye Bye Good Deepank abc"
b = "Hi"
# count occurences a string in other string
print(a.count(b)) 
b = "Bye"
# check if a string occurs in other string
# string not found return -1
print(a.find(b)) 
# replace string in other string
replaced = a.replace(' ','--')
print(replaced)
# string in upper case
print(a.upper())
# string in lower case
print(a.lower())

print()
print('... LOOP IN STRINGS ... ')
a = "Hi Hi Hello Bye Bye Good Deepank abc"
for c in a:
	print(c, end=',')
