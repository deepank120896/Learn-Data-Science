def is_palindrome(w):
	w = w.lower()
	return w[::-1] == w

while True:
	word = input('\nEnter Word (\'q\' to quit): ')
	if word == 'q':
		break
	if is_palindrome(word) == True:
		print(word, 'is palindrome')
	else:
		print(word, 'is NOT palindrome')
