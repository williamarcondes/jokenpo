import random
from papel import papel
from tesoura import tesoura
from pedra import pedra

def resultado(user, computer):
    if computer == user:
        return "Empataram"
    
    if [computer, user] == [0, 2]:
        return "Você perdeu, pedra quebra a tesoura"

    if [computer, user] == [2, 1]:
        return "Você perdeu, tesoura corta o papel"

    if [computer, user] == [1, 0]:
        return "Você perdeu, papel enrola a pedra"
    
    return "Você venceu"

def game(user):
    if not user.isdigit():
        return "Digito incorreto"
    
    user = int(user)
    if not user in range(0,3):
        return "Informe um número entre 0 e 2"
    
    computer = random.randint(0,2)

    dicionario_escolhas = {0: pedra(), 1: papel() , 2: tesoura()}

    print(f"Você escolheu: {user} {dicionario_escolhas[user]}")
    print(f"Computador escolheu: {computer} {dicionario_escolhas[computer]}")

    return resultado(user, computer)


user = input("Qual sua escolha? [0: PEDRA, 1: PAPEL, 2: TESOURA]")

print(game(user))