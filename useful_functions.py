import os

def clear():
## CLEARS CONSOLE
## NOTE that there are different commands for Windows and Unix-based system (Mac and Linux)
    if os.name == 'nt': os.system('cls') # Windows
    else: os.system('clear') # Unix

print(os.name)