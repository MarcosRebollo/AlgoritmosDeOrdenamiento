from shell_sort import shell_sort

# Ejemplo de ordenamiento de números
if __name__ == "__main__":
    # Ejemplo con lista pequeña
    numeros_pequeños = [64, 34, 25, 12, 22, 11, 90]
    print("Lista pequeña original:", numeros_pequeños)
    lista_ordenada = shell_sort(numeros_pequeños.copy())
    print("Lista pequeña ordenada:", lista_ordenada)
    
    # Ejemplo con lista mediana
    numeros_medianos = [23, 29, 15, 19, 31, 7, 9, 5, 2, 1, 12, 18, 24, 28]
    print("\nLista mediana original:", numeros_medianos)
    lista_ordenada = shell_sort(numeros_medianos.copy())
    print("Lista mediana ordenada:", lista_ordenada)
    
    # Ejemplo con lista grande
    import random
    numeros_grandes = [random.randint(1, 1000) for _ in range(30)]
    print("\nLista grande original:", numeros_grandes)
    lista_ordenada = shell_sort(numeros_grandes.copy())
    print("Lista grande ordenada:", lista_ordenada)
    
    # Verificar si está ordenada
    print("\nVerificación de ordenamiento:",
          "Correcto" if all(lista_ordenada[i] <= lista_ordenada[i+1] 
                           for i in range(len(lista_ordenada)-1)) else "Incorrecto")
