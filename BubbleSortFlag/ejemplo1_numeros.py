from bubble_sort_flag import bubble_sort_flag

# Ejemplo de ordenamiento de números con detección temprana
if __name__ == "__main__":
    # Lista desordenada de números
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", numeros)
    
    # Aplicar bubble sort con señal
    lista_ordenada = bubble_sort_flag(numeros.copy())
    
    print("Lista ordenada:", lista_ordenada)
    
    # Caso con lista casi ordenada
    casi_ordenada = [1, 2, 3, 5, 4, 6, 7, 8]
    print("\nLista casi ordenada original:", casi_ordenada)
    
    lista_ordenada = bubble_sort_flag(casi_ordenada.copy())
    print("Lista casi ordenada después de ordenar:", lista_ordenada)
