# February 27,2019
# Trying to create a dice rolling simulator

from random import randint

while True:
	number = randint(1,6)
	print(number)
	rollAgain = input("Do you want to roll again?")

# Have to put quotations around yes to be able to run in terminal
	if rollAgain is "yes":
		continue
	else:
		print("quitting now...")
		break
