def is_Anagram(w1,w2):
	w1 = w1.lower()
	w2 = w2.lower()
	return sorted(w1) == sorted(w2)

while True:
	print("\nEnter 2 words:-> ")
	w1 = input(" First Word: ")
	w2 = input(" Second Word: ")
	if w1 == 'quit' or w2 =='quit':
		break
	elif is_Anagram(w1,w2) == True:
		print(w1,w2, 'are Anagrams')
	else:
		print(w1,w2, 'are NOT Anagrams')
