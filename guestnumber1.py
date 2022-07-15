import random

# La computadora debe adivinar el número seleccionado por el jugador.
def my_number(x):

    print("Juega a adivina el número")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.")

    lower_limit = 1
    upper_limit = x
    answer = ""

    while answer != "si":
        if lower_limit != upper_limit:
            guest = random.randint(lower_limit, upper_limit)
        else:
            guest = lower_limit  
        
        respuesta = input(f"Mi predicción es {guest}. ¿Es correcta? SI/NO ").lower()
        if respuesta !="si":
            pregunta = input(f'Si es muy alta, ingresa (-). Si es muy baja, ingresa (+).')       
            if pregunta == "-":
                lower_limit = guest - 1
            elif pregunta == "+":
                upper_limit = guest + 1

    print(f"La computadora adivinó tu número correctamente: {guest}")


my_number(15)