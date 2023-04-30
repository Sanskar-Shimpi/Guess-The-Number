from colorama import Fore, Back, Style
sLine = lambda: "-----------------------------------------------------------"
wMessage = "Welcome To Game!"
print(wMessage.center(56), sLine(), sep = "\n")
print("\nIt is number guessing game!".upper())
ANSWER = 90
try:
	while(ANSWER):
		uC = int(input("\nYour Guess: "))
		print(Fore.YELLOW)
		if(uC != ANSWER):
			print(sLine())
			print("\nWrong Guess!\n")
			print(sLine())
			print(Style.RESET_ALL)
		else:
			print(Fore.GREEN)
			print(sLine())
			print("\n★You Won!★".center(50).upper())
			ANSWER = 0
			print(Style.RESET_ALL)
			print("\nTHANK YOU!\n")
			print(Fore.GREEN, sLine(), Style.RESET_ALL)
					
except:
	print("\nWrong Input!")