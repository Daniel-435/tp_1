from typing import List


def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
    """
    tablero = []
    for f in range(n_filas) :
        fila = []
        for c in range(n_columnas) :
            fila.append(" ")
        tablero.append(fila)
    return tablero

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    
    contador = 0
    for f in range(len(tablero)):
        for c in range(len(tablero[f])) :
            if tablero[f][c] != " " : contador += 1
    if  contador%2 == 0 : return True
    return False

def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """
    if not(-1< columna < len(tablero[0])):return False
    n = len(tablero) - 1
    for i in range(len(tablero)) :
        if tablero[n - i][columna] == " " : 
            if es_turno_de_x(tablero) :
                tablero[n - i][columna] = "X"
            else:
                tablero[n - i][columna] = "O"
            return True
    return False


def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    for f in range(len(tablero)):
        for c in range(len(tablero[f])) :
            if tablero[f][c] == " " : return False
    return True

def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`

    EJEMPLO: para el siguiente tablero, el ganador es 'X' por tener un cuatro en
    línea en diagonal
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', 'X', ' ', ' '],
            [' ', 'O', 'O', 'X', 'X', 'X', 'O'],
        ]
    """
    cadena_1 = ""
    cadena_2 = ""
    diagonal_1 = ""
    diagonal_2 = ""
    for fil in range(len(tablero)):
        for col in range(len(tablero[fil])) : 
            cadena_1 += tablero[fil][col]
            if "XXXX" in cadena_1 : return "X"
            if "OOOO" in cadena_1 : return "O"
            for n in range(4) :
                #condiciones necesarias para la horizontal
                if fil < (len(tablero) - 3 ) :
                    cadena_2 += tablero[fil + n][col] 
                #condiciones necesarias para la diagonal
                if col < (len(tablero[0]) - 3) and fil < (len(tablero) - 3 ) :
                    diagonal_1 += tablero[n + fil][n + col]
                #condiciones necesarias para la diagonal inversa
                if col > 2 and fil < (len(tablero) - 3 ) :
                    diagonal_2 += tablero[n + fil][col - n]
                if "XXXX" in diagonal_1 or "XXXX" in diagonal_2 : return "X"
                if "OOOO" in diagonal_1 or "OOOO" in diagonal_2 : return "O"
                if "XXXX" in cadena_2 : return "X"
                if "OOOO" in cadena_2 : return "O"
            diagonal_1 = ""
            diagonal_2 = ""
            cadena_2 = ""
        cadena_1 = ""
    return " "