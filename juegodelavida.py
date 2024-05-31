import copy, random, sys, time


def iniciar_juego():
    """
    Inicia el Juego de la Vida de Conway.

    Permite al usuario elegir el tamaño de la cuadrícula y el carácter que representa una célula viva.
    """

    # Pedir al usuario el tamaño de la cuadrícula
    while True:
        try:
            ANCHO = int(input("Introduce el ancho de la cuadrícula: "))
            ALTO = int(input("Introduce el alto de la cuadrícula: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Pedir al usuario el carácter para las células vivas
    VIVO = input("Introduce el carácter para indicar una célula viva (por defecto 'O'): ")
    if not VIVO:
        VIVO = 'O'  # Si no se introduce ningún carácter, usar el valor por defecto
    MUERTO = ' '  # Carácter para la célula muerta

    # Las variables celulas y siguientesCelulas son diccionarios que contienen
    # el estado actual del juego y el siguiente.
    # Las claves del diccionario son tuplas que pueden tener el valor VIVO o MUERTO
    siguientesCelulas = {}

    # Asignar valores aleatorios a las células iniciales
    for x in range(ANCHO):
        for y in range(ALTO):
            # 50% de posibilidades de estar viva o muerta
            if random.randint(0, 1) == 0:
                siguientesCelulas[(x, y)] = VIVO
            else:
                siguientesCelulas[(x, y)] = MUERTO

    while True:  # bucle principal del programa
        """
        Cada iteración de este bucle es una generación de la simulación del juego de la vida.
        """
        print('\n' * 50)  # Separación entre generaciones
        celulas = copy.deepcopy(siguientesCelulas)

        # Imprimir las células por pantalla
        for y in range(ALTO):
            for x in range(ANCHO):
                print(celulas[(x, y)], end='')
            print()
        print('Pulsa Ctrl-C para parar.')

        # Calcular la nueva generación de células en función de los valores actuales
        for x in range(ANCHO):
            for y in range(ALTO):
                # Obtener las coordenadas de las vecinas incluso si están en el límite
                izquierda = (x - 1) % ANCHO
                derecha = (x + 1) % ANCHO
                arriba = (y - 1) % ALTO
                abajo = (y + 1) % ALTO

                # Calcular el número de células vecinas vivas
                numVecinasVivas = 0
                if celulas[(izquierda, arriba)] == VIVO:
                    numVecinasVivas += 1
                if celulas[(x, arriba)] == VIVO:
                    numVecinasVivas += 1
                if celulas[(derecha, arriba)] == VIVO:
                    numVecinasVivas += 1
                if celulas[(izquierda, y)] == VIVO:
                    numVecinasVivas += 1
                if celulas[(derecha, y)] == VIVO:
                    numVecinasVivas += 1
                if celulas[(izquierda, abajo)] == VIVO:
                    numVecinasVivas += 1
                if celulas[(x, abajo)] == VIVO:
                    numVecinasVivas += 1
                if celulas[(derecha, abajo)] == VIVO:
                    numVecinasVivas += 1

                # Basar el valor de la nueva generación en función
                # de los valores actuales
                if celulas[(x, y)] == VIVO and (numVecinasVivas == 2 or numVecinasVivas == 3):
                    # Células vivas con 2 o 3 vecinas vivas permanecen vivas
                    siguientesCelulas[(x, y)] = VIVO
                elif celulas[(x, y)] == MUERTO and numVecinasVivas >= 2:
                    # Células muertas con 2 o más vecinas vivas cobran vida
                    siguientesCelulas[(x, y)] = VIVO
                else:
                    # En cualquier otro caso continúan muertas
                    siguientesCelulas[(x, y)] = MUERTO

        try:
            time.sleep(1)  # Añadir un segundo de pausa para evitar parpadeos
        except KeyboardInterrupt:
            print("Juego de la vida de Conway")
            print("https://es.wikipedia.org/wiki/Juego_de_la_vida")
            sys.exit()  # Cuando se pulsa CTRL+C termina el programa


if __name__ == "__main__":
    iniciar_juego()