from bubble_sort_flag import bubble_sort_flag

def ordenar_palabras(palabras):
    return bubble_sort_flag(list(palabras))

# Ejemplo de ordenamiento de strings con casos parcialmente ordenados
if __name__ == "__main__":
    # Lista parcialmente ordenada de palabras
    palabras = ["ana", "carlos", "diana", "eduardo", "bernardo"]
    
    print("Lista original de palabras:", palabras)
    
    # Aplicar bubble sort con señal
    palabras_ordenadas = ordenar_palabras(palabras)
    
    print("Lista ordenada de palabras:", palabras_ordenadas)
    
    # Caso con lista casi ordenada alfabéticamente
    casi_ordenada = ["amarillo", "azul", "morado", "negro", "rojo", "verde", "violeta"]
    print("\nLista casi ordenada original:", casi_ordenada)
    
    palabras_ordenadas = ordenar_palabras(casi_ordenada)
    print("Lista ordenada:", palabras_ordenadas)
