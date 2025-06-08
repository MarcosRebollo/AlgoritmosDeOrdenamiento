from selection_sort import selection_sort

# Ejemplo de ordenamiento de números
if __name__ == "__main__":
    # Lista desordenada de números
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", numeros)
    
    # Aplicar selection sort
    lista_ordenada = selection_sort(numeros.copy())
    
    print("Lista ordenada:", lista_ordenada)
    
    # Caso con números duplicados
    numeros_duplicados = [64, 34, 25, 12, 22, 11, 90, 34, 25]
    print("\nLista con números duplicados:", numeros_duplicados)
    
    lista_ordenada = selection_sort(numeros_duplicados.copy())
    print("Lista ordenada:", lista_ordenada)
    
    # Caso con números negativos
    numeros_negativos = [64, -34, 25, -12, 22, -11, 90]
    print("\nLista con números negativos:", numeros_negativos)
    
    lista_ordenada = selection_sort(numeros_negativos.copy())
    print("Lista ordenada:", lista_ordenada)
