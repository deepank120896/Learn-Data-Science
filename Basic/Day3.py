# Usage of if-elif-else and while-loop
import random

r = random.randint(1,20)

while True :
	inp = int(input(" Guess the number (1-20): "))

	if inp < r:
		print(" Wrong guess, Try a BIGGER number...")
	elif inp > r:
		print(" Wrong guess, Try a SMALLER number...")
	else:
		print(" Correct guess ...")
		break
