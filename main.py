from colorama import Fore, Back, Style
import colorama
colorama.init()
import os


#открытие файла с настройками


#очистка консоли
def clearShell():
    os.system(['clear', 'cls'][os.name == os.sys.platform])

def find_bank(what):
    for i in all_banks:
        if i.name == what:
            return i

class Bank:  #банка
    def __init__(self, name, MAX, l):
        self.name = name
        self.MAX = MAX
        self.l = l

    def print(self):
        listt = list(range(self.MAX))
        listt.reverse()
        for i in listt:
            if i >= self.l:
                print(Back.CYAN + "│" + Back.RESET + Fore.BLUE + "      ", Fore.RESET + Back.CYAN + "│" + Back.RESET)
            else:
                print(Back.CYAN + "│" + Back.RESET +Fore.BLUE + "≋≋≋≋≋≋≋" + Fore.RESET + Back.CYAN + "│" + Back.RESET)
        print(Fore.CYAN + "▔▔▔▔▔▔▔▔" + Fore.RESET)
        print("    " + self.name )
        print(Style.BRIGHT + 
        Fore.RED + 
        "{0}" + 
        Fore.RESET + 
        Fore.GREEN + 
        "из" + Fore.RESET
        + Fore.RED + "{1}" + Fore.RESET.format(self.l, self.MAX))
        print()
        
print(Style.BRIGHT, end="")

all_banks = [Bank("A", 7, 4), Bank("B", 5, 0), Bank("C", 4, 0)]
all_banks_names = ["A", "B", "C"]
while True:
    for i in all_banks:
        i.print()
    command = input(Fore.RED + "Команда: "+ Fore.RESET + Fore.GREEN)
    command_split = command.split()
    if command_split[0] in all_banks_names:
        one_lit = find_banks(command_split[0])
        pass
        
      
    clearShell()
