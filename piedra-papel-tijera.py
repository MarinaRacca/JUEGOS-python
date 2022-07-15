import random

#juego piedra papel o tijera
def game():
    user = input("Escoge una opción: '0' para piedra, '1' para papel, '2' para tijera.\n").lower()
    computer = random.choice(['0', '1', '2'])

    if user == computer:
        return '¡Empate!'

    if user_wins(user, computer):
        return '¡Ganaste!'

    return '¡Perdiste!'


def user_wins(player, opponent):
    # Piedra > Tijera  
    # Papel > Piedra 
    # Tijera > Papel
    if ((player == '0' and opponent == '2')
        or (player == '1' and opponent == '1')
        or (player == '2' and opponent == '0')):
        return True
    else:
        return False


print(game())