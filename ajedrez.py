"""
La clase tablero define como una matrez 8x8 el tablero de juego y lo 
inicializa con la posición origen de todas las piezas
"""
class Tablero:
    def __init__(self):
        self.tablero = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
#Imprimo el tablero con un espacio entre cada fila para que quede mejor
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" ".join(fila))
        print()

"""
La clase pieza es el padre del resto de clases pieza, es decir el resto de clases pieza 
heredan de ella y están obligadas a implementar el método mover con la lógica correspondiente
a cada tipo de pieza.
"""
class Pieza:
    def __init__(self, color):
        self.color = color

    def mover(self, origen, destino, tablero):
        pass

"""
La clase peon hereda de la clase Pieza y en ella se implementa la función mover
con la lógica de movimiento del peon que en este caso tiene una función especial  
cuando se encuentra en su posición incial.
La lógica esta simplificada ignorando la posibilidad de que haya piezas en medio y sin 
que se pueda realizar la acción de comer ni la accion de comer al paso
"""
class Peon(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if self.color == 'blanco':
            direccion = -1
        else:
            direccion = 1

        # Movimiento inicial de dos casillas
        if (fila_origen == 6 and self.color == 'blanco') or (fila_origen == 1 and self.color == 'negro'):
            if fila_destino == fila_origen + 2 * direccion and columna_destino == columna_origen and tablero[fila_destino][columna_destino] == ' ':
                tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
                tablero[fila_origen][columna_origen] = ' '
                return True

        # Movimiento normal de una casilla
        if fila_destino == fila_origen + 1 * direccion and columna_destino == columna_origen and tablero[fila_destino][columna_destino] == ' ':
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
La clase torre hereda de la clase Pieza y en ella se implementa la función mover
con la lógica de movimiento de la torre que se basa en que o se mantiene la misma fila
o se mantiene la misma columna.
La lógica esta simplificada ignorando la posibilidad de que haya piezas en medio y sin 
que se pueda realizar la acción de comer
"""
class Torre(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if fila_origen == fila_destino or columna_origen == columna_destino and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para una torre
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False


"""
La clase caballo hereda de la clase Pieza y en ella se implementa la función mover
con la lógica de movimiento del caballo haciendo que sus posibles movimientos trazen una "L"
La lógica esta simplificada ignorando la posibilidad de que haya piezas en medio y sin 
que se pueda realizar la acción de comer
"""
class Caballo(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        movimientos_posibles = [
            (fila_origen + 2, columna_origen + 1),
            (fila_origen + 2, columna_origen - 1),
            (fila_origen - 2, columna_origen + 1),
            (fila_origen - 2, columna_origen - 1),
            (fila_origen + 1, columna_origen + 2),
            (fila_origen + 1, columna_origen - 2),
            (fila_origen - 1, columna_origen + 2),
            (fila_origen - 1, columna_origen - 2),
        ]

        if (fila_destino, columna_destino) in movimientos_posibles and tablero[fila_destino][columna_destino] == ' ':
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
La clase alfil hereda de la clase Pieza y en ella se implementa la función mover
con la lógica de movimiento del alfil para lo cual se calcula la diferencia entre las
coordenadas de cada eje y esta tiene que ser igual
La lógica esta simplificada ignorando la posibilidad de que haya piezas en medio y sin 
que se pueda realizar la acción de comer
"""
class Alfil(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if abs(fila_destino - fila_origen) == abs(columna_destino - columna_origen) and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para un alfil
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
La clase Reina hereda de la clase Pieza y en ella se implementa la función mover
con la lógica de movimiento de la reina que implementa la logica de la torre o la del alfil
La lógica esta simplificada ignorando la posibilidad de que haya piezas en medio y sin 
que se pueda realizar la acción de comer
"""
class Reina(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if (fila_origen == fila_destino or columna_origen == columna_destino or abs(fila_destino - fila_origen) == abs(columna_destino - columna_origen)) and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para una reina
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
La clase Rey hereda de la clase Pieza y en ella se implementa la función mover
con la lógica de movimiento de la rey que implementa la logica reina pero limitada a una casilla
de distancia.
La lógica esta simplificada ignorando la posibilidad de que se pueda realizar la acción de comer
y sin la acción de enrocarse.
"""
class Rey(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if abs(fila_destino - fila_origen) <= 1 and abs(columna_destino - columna_origen) <= 1 and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para un rey
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
La clase jugador sirve para distinguir entre el jugador blanco y el negro.
"""
class Jugador:
    def __init__(self, color):
        self.color = color

"""
La clase juego será con la que se inicie el juego determinando
un jugador blanco y uno negro y será la clase en la que se meterá todo lo relacionado
con la partida de ajedrez ya que se crean las preguntas que se va haciendo a los
jugadores en cada movimiento. Contiene el tablero y los jugadores
"""
class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_blanco = Jugador('blanco')
        self.jugador_negro = Jugador('negro')
    #Solicita los movimientos al jugador comprobando que sean posiciones válidas
    #Se identifica la pieza que se va a mover en función de la posición de origen,
    #instanciandose una pieza de la clase correspondiente
    def jugar(self):
        turno = 1
        while True:
            print(f"Turno {turno}")
            self.tablero.imprimir_tablero()

            jugador_actual = self.jugador_blanco if turno % 2 == 1 else self.jugador_negro
            origen = self.obtener_coordenadas("Elija la posición de la pieza que desea mover:")
            pieza = self.elegir_pieza(jugador_actual, origen, self.tablero.tablero)
            while  not pieza:
                origen = self.obtener_coordenadas("Elija la posición de la pieza que desea mover:")
                pieza = self.elegir_pieza(jugador_actual, origen, self.tablero.tablero)

            if pieza:
                
                movimiento_valido = False
                while not movimiento_valido:              
                    destino = self.obtener_coordenadas("Elija la posición a la que desea mover la pieza:")
                    movimiento_valido = self.validar_movimiento(pieza, origen, destino)

                pieza.mover(origen, destino, self.tablero.tablero)
                turno += 1
    
    def elegir_pieza(self, jugador, Posicion_pieza, mi_tablero):
        #obtenemos la pieza de la posicion dada y se instancia de la clase derivada correspondiente
        valor_1 = Posicion_pieza[0]
        valor_2 = Posicion_pieza[1]
        if jugador.color != "blanco": 
            if mi_tablero [valor_1][valor_2] == "♟":
                return Peon(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♜":
                return Torre(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♞":
                return Caballo(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♝":
                return Alfil(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♛":
                return Reina(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♚":
                return Rey(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == " ":
                return
        else:    
            if mi_tablero [valor_1][valor_2] == "♙":
                return Peon(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♖":
                return Torre(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♘":
                return Caballo(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♗":
                return Alfil(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♕":
                return Reina(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♔":
                return Rey(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == " ":
                return
    


    def obtener_coordenadas(self, mensaje):
        fila = int(input(f"{mensaje} Fila: ")) - 1
        columna = int(input(f"{mensaje} Columna: ")) - 1
        return fila, columna

    def validar_movimiento(self, pieza, origen, destino):
        return pieza.mover(origen, destino, self.tablero.tablero)

juego = Juego()
juego.jugar()

