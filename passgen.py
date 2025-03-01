import random 
import string
import time
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
def generate_random_string():
    while True:
        try:
            length = int(input("Quantidade de caracteres da senha (min 7): "))
            clear_terminal()
            if length <= 6:
                print('\033[91mErro: A senha deve ter pelo menos 7 caracteres.\033[0m')
            else:
                break
        except ValueError:
            print('\033[91mErro! Digite um número válido.\033[0m')
    clear_terminal()

    while True:
        special_chars = input("Special caracteres? (y/n): ").lower()
        if special_chars in ["y", "n"]:
            break
        print("\033[91mErro: Digite 'y' para sim ou 'n' para não.\033[0m")
        
        
        
    clear_terminal()

    
    caracters = string.ascii_letters + string.digits

    if special_chars == "y":
        caracters += string.punctuation
    password = ''.join(random.choice(caracters) for i in range(length))

    return password
    


password_generated = generate_random_string() 

for n in range(3):
    print('Generating Password' + '.' * (n + 1))
    time.sleep(0.25)
    clear_terminal()
print(f"Genereted Password:  \033[93m{password_generated}\033[00m")


