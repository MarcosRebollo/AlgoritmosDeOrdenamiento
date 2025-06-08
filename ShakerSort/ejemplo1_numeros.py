from shaker_sort import shaker_sort

# Ejemplo de ordenamiento de números
if __name__ == "__main__":
    # Lista desordenada de números
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", numeros)
    
    # Aplicar shaker sort
    lista_ordenada = shaker_sort(numeros.copy())
    
    print("Lista ordenada:", lista_ordenada)
    
    # Caso especial con "tortugas" (números pequeños al final)
    lista_tortugas = [90, 80, 70, 60, 50, 40, 30, 1]
    print("\nLista con 'tortuga' al final:", lista_tortugas)
    
    lista_ordenada = shaker_sort(lista_tortugas.copy())
    print("Lista ordenada:", lista_ordenada)
