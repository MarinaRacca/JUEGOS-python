import random #python docs random module

#El jugador debe adivinar el número seleccionado por la computadora
def guestnumber(x):
    print("Juega a adivina el número")
    print("Tu objetivo es adivinar el número generado por la computadora")

    number = random.randint(1,x) # random integer >=1

    guest = 0

    while guest != number:

        guest = int(input(f'Adivina el número'))

        if guest < number:
            print ("Incorrecto, intenta de nuevo")
            print ("Pista: el núnmero es más grande")

        elif guest > number: 
            print("Incorrecto, intenta de nuevo")
            print("Pista: El número es más pequeño")    
    
    print(f'El número {number} es correcto. Felicitaciones, ganaste el juego')

guestnumber(15)

