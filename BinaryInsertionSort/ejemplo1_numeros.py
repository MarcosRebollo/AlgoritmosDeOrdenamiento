from binary_insertion_sort import binary_insertion_sort

# Ejemplo de ordenamiento de números
if __name__ == "__main__":
    # Lista desordenada de números
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", numeros)
    
    # Aplicar binary insertion sort
    lista_ordenada = binary_insertion_sort(numeros.copy())
    
    print("Lista ordenada:", lista_ordenada)
    
    # Caso con números negativos
    numeros_negativos = [64, -34, 25, -12, 22, 11, -90]
    print("\nLista con negativos original:", numeros_negativos)
    
    lista_ordenada = binary_insertion_sort(numeros_negativos.copy())
    print("Lista con negativos ordenada:", lista_ordenada)
    
    # Caso con números duplicados
    numeros_duplicados = [64, 34, 25, 12, 22, 11, 90, 34, 25]
    print("\nLista con duplicados original:", numeros_duplicados)
    
    lista_ordenada = binary_insertion_sort(numeros_duplicados.copy())
    print("Lista con duplicados ordenada:", lista_ordenada)
