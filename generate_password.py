
from random import randint, choice, shuffle, sample
import string
from os import system

def generate_pass(upper: bool, lower: bool, number: bool, special: bool, length: int):
    char=''
    if upper:
        char += string.ascii_uppercase
    if lower:
        char += string.ascii_lowercase
    if number:
        char += string.digits
    if special:
        char += string.punctuation
    char = [*char]
    shuffle(char)
    while True:
        if (len(char) < length):
            char += shuffle(char)
        else:
            break
    res = sample(char, length)
    password = ''
    for i in res:
        password +=str(i)
    return password


def main():
    while True:
        check_char = True
        system('cls')
        header = "============== GERADOR SENHA by Paulo ==============\n"
        print(header)
        # Set Uppercase
        while(True):
            upper = input("Usar caracteres maiusculos (y/n)? ")
            if upper == 'y' or upper == 'n':
                upper = True if upper == 'y' else False
                break
            else:
                system('cls')
                print(header)
                print('**Valor nao permitido')
                pass
        # Set lowercase
        while(True):
            lower = input("Usar caracteres minusculos (y/n)? ")
            if lower == 'y' or lower == 'n':
                lower = True if lower == 'y' else False
                break
            else:
                system('cls')
                print(header)
                print('**Valor nao permitido')
                pass
        # Set Numbers
        while(True):
            numbers = input("Usar numeros (y/n)? ")
            if numbers == 'y' or numbers == 'n':
                numbers = True if numbers == 'y' else False
                break
            else:
                system('cls')
                print(header)
                print('**Valor nao permitido')
                pass
        # Set Specials
        while(True):
            special = input("Usar caracteres especiais (y/n)? ")
            if special == 'y' or special == 'n':
                special = True if special == 'y' else False
                break
            else:
                system('cls')
                print(header)
                print('**Valor nao permitido')
                pass
        # Verify check char
        if (special == False
            and upper == False
            and lower == False
            and numbers == False):
                check_char = False
                print('\n**Nenhum tipo de caractere selecionado\n')

        if check_char:
            # Length Password
            while(True):
                length = input("Tamanho da senha: ")
                try:
                    length = int(length)
                except:
                    system('cls')
                    print(header)
                    print('**Valor nao permitido')
                    pass
                if length == 0:
                    system('cls')
                    print(header)
                    print('**Valor nao permitido')
                    pass
                elif isinstance(length, int):
                    break
                else:
                    system('cls')
                    print(header)
                    print('**Valor nao permitido')
                    pass
            password = generate_pass(upper, lower, numbers, special, length)
            print(password)

        while(True):
            newpass = ''
            newpass = input('Deseja gerar outra senha (y/n)? ')
            if newpass == 'y' or newpass == 'n':
                newpass = True if newpass == 'y' else False
                break
            else:
                system('cls')
                print(header)
                print('**Valor nao permitido')
                pass
        if newpass == True:
            pass
        elif newpass == False:
            break
    system('cls')
    system('exit')

main()