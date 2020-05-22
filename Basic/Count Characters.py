def count_characters(string):
	count = {}
	for char in string:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1
	print(count)

string = input("Enter a string: ")
count_characters(string)
