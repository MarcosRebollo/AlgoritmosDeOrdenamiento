from bubble_sort import bubble_sort

# Ejemplo de ordenamiento de números
if __name__ == "__main__":
    # Lista desordenada de números
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", numeros)
    
    # Aplicar bubble sort
    lista_ordenada = bubble_sort(numeros.copy())
    
    print("Lista ordenada:", lista_ordenada)
    
    # Caso con números negativos
    numeros_negativos = [64, -34, 25, -12, 22, 11, -90]
    print("\nLista con negativos original:", numeros_negativos)
    
    lista_ordenada = bubble_sort(numeros_negativos.copy())
    print("Lista con negativos ordenada:", lista_ordenada)
