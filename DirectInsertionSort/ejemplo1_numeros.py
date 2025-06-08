from insertion_sort import insertion_sort

# Ejemplo de ordenamiento de números
if __name__ == "__main__":
    # Lista desordenada de números
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", numeros)
    
    # Aplicar insertion sort
    lista_ordenada = insertion_sort(numeros.copy())
    
    print("Lista ordenada:", lista_ordenada)
    
    # Caso con lista casi ordenada
    casi_ordenada = [1, 2, 3, 5, 4, 6, 7, 8]
    print("\nLista casi ordenada original:", casi_ordenada)
    
    lista_ordenada = insertion_sort(casi_ordenada.copy())
    print("Lista casi ordenada después de ordenar:", lista_ordenada)
    
    # Caso con números negativos y positivos
    mixta = [3, -1, 4, -5, 9, -2, 6, 0]
    print("\nLista con números positivos y negativos:", mixta)
    
    lista_ordenada = insertion_sort(mixta.copy())
    print("Lista ordenada:", lista_ordenada)
