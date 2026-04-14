import random
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "="*35)
print(Fore.YELLOW + " WELCOME TO LUCKY DRAW ")
print(Fore.CYAN + "="*35)

def luckydraw():
    a = int(input(Fore.YELLOW + "\nEnter the number between 10 to 20 : "))

    if (a > 9 and a < 21):

        selected = random.choice([13, 15, 16, 19])

        if (a == selected):

            print(Fore.GREEN + "-"*35)
            print(Fore.GREEN + "CONGRATULATIONS")
            print(Fore.GREEN + "-"*35)

            if selected == 13:
                print(Fore.YELLOW + "\nyou wone: $100")
            elif selected == 16:
                print(Fore.YELLOW + "\nyou wone: $1000")
            elif selected == 19:
                print(Fore.YELLOW + "\nyou wone: $10000")
            elif selected == 15:
                print(Fore.YELLOW + "\nyou wone: $50000")

            input(Fore.CYAN + "\nPress Enter to continue...")

            print(Fore.MAGENTA + "*"*35)
            print(Fore.CYAN + "The lucky number was : ", selected)
            print(Fore.MAGENTA + "*"*35)

            print(Fore.YELLOW + "\nIf you want to restart the game press : y")
            print("If you want to exit press any other key :")
            z = input(Fore.GREEN + "\nwhats your choise : ")

            if z == 'y':
                luckydraw()
            else:
                print(Fore.MAGENTA + "*"*35)
                print(Fore.GREEN + "Thank you")
                print(Fore.MAGENTA + "*"*35)

        else:
            print(Fore.RED + "-"*35)
            print(Fore.RED + "OOPS! TRY NEXT TIME ")
            print(Fore.RED + "-"*35)

    else:
        print(Fore.RED + "Your Number is not within the range")

print(Fore.GREEN + "\n Available Gifts ")
print(Fore.WHITE + "-"*30)
print(Fore.CYAN +
    "N.o 13 : $100\n"
    "N.o 16 : $1000\n"
    "N.o 19 : $10000\n"
    "N.o 15 : $50000\n")
print(Fore.WHITE + "-"*30)

luckydraw()

input("\nProgram finished. Press Enter to exit...")
