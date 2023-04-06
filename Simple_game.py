import random

def adivina_el_numero():
    print("Bienvenido al juego 'Adivina el número'")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Tienes 10 intentos para adivinarlo.\n")

    numero_secreto = random.randint(1, 100)
    intentos = 10

    while intentos > 0:
        print(f"Te quedan {intentos} intentos.")
        try:
            adivinanza = int(input("Adivina el número: "))
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            continue

        if adivinanza == numero_secreto:
            print(f"¡Felicitaciones! Adivinaste el número secreto: {numero_secreto}")
            break
        elif adivinanza < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

        intentos -= 1

    if intentos == 0:
        print(f"\nLo siento, no adivinaste el número. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivina_el_numero()
