import time
import os
import random
from termcolor import colored, cprint

logo = colored('''  

  ____      _           _____         _
 / ___|___ | | ___  _ _|_   _|__  ___| |_
| |   / _ \| |/ _ \| '__|| |/ _ \/ __| __|
| |__| (_) | | (_) | |   | |  __/\__ \ |_
 \____\___/|_|\___/|_|   |_|\___||___/\__|

''', 'green')

def start():
	os.system('clear')
	cprint(logo)
	print("This tests your computer's ability to render colors") 
	input("Press enter to start")
	print("")

def main():
	start()
	for x in range(30):
		number = random.randint(1, 8)
		if number == 1:
			color = 'blue'
		elif number == 2:
			color = 'red'
		elif number == 3:
			color = 'green'
		elif number == 4:
			color = 'yellow'
		elif number == 5:
			color = 'blue'
		elif number == 6:
			color = 'magenta'
		elif number == 7:
			color = 'cyan'
		elif number == 8:
			color = 'white'

		cprint(color, color)
		time.sleep(2)

main()
