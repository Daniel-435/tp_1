import cuatro_en_linea
def muestra_el_tablero(tablero) :
    for i in range(len(tablero[0])) :
        print(f"|{i}",end="")
    print("|")
    print("_"*((len(tablero[0]) + 1)*2))
    #print("_"*((len(tablero))+1)*2)
    print("")
    for i in range(len(tablero)) :
        fila = "|".join(tablero[i])
        print(f"|{fila}|")

def mensaje_de_opcion_invalida() :
    print("opcion invalida, vuelva a intentar")

def main() :
    while True :
        ancho = input("ingrese el ancho del juego entre 4 y 10: ")
        if ancho.isdigit() and 3 < int(ancho) < 11 : break
        mensaje_de_opcion_invalida()
    while True :
        alto = input("ingrese el alto del juego entre 4 y 10 : ")
        if alto.isdigit() and 3 < int(alto) < 11 : break
        mensaje_de_opcion_invalida()
    tablero = cuatro_en_linea.crear_tablero(int(alto), int(ancho))
    muestra_el_tablero(tablero)
    while True :
        if cuatro_en_linea.es_turno_de_x(tablero) : turno = "X"
        else :
            turno = "O"
        columna = input(f"columna para insertar {turno} entre 0 y {len(tablero[0]) - 1} \n o ingrese S para finalizar:  ")
        if columna.lower() == "s" : break
        if not(columna.isdigit() and 0 <= int(columna) < len(tablero[0])) :
            mensaje_de_opcion_invalida()
            continue
        if cuatro_en_linea.insertar_simbolo(tablero, int(columna)) :
            muestra_el_tablero(tablero)
            if cuatro_en_linea.obtener_ganador(tablero) == "X" : return print("gano X!")
            if cuatro_en_linea.obtener_ganador(tablero) == "O" : return print("gano Y!")
            if cuatro_en_linea.tablero_completo(tablero) : return print("no hay ganadores")
        else : 
            muestra_el_tablero(tablero)
            continue
main()
