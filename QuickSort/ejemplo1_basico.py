from quick_sort import quick_sort

def mostrar_ejemplos():
    # Ejemplo con números enteros
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista de números original:", numeros)
    numeros_ordenados = quick_sort(numeros.copy())
    print("Lista de números ordenada:", numeros_ordenados)
    
    # Ejemplo con números flotantes
    flotantes = [3.14, 1.41, 2.71, 0.58, 1.73, 2.24]
    print("\nLista de flotantes original:", flotantes)
    flotantes_ordenados = quick_sort(flotantes.copy())
    print("Lista de flotantes ordenada:", flotantes_ordenados)
    
    # Ejemplo con strings
    palabras = ["python", "java", "ruby", "go", "rust"]
    print("\nLista de palabras original:", palabras)
    palabras_ordenadas = quick_sort(palabras.copy())
    print("Lista de palabras ordenada:", palabras_ordenadas)
    
    # Ejemplo con lista grande
    import random
    lista_grande = [random.randint(1, 1000) for _ in range(100)]
    print("\nLista grande (primeros 10 elementos):", lista_grande[:10], "...")
    lista_grande_ordenada = quick_sort(lista_grande.copy())
    print("Lista grande ordenada (primeros 10 elementos):", 
          lista_grande_ordenada[:10], "...")
    
    # Verificación de ordenamiento
    print("\nVerificación de ordenamiento:",
          "Correcto" if all(lista_grande_ordenada[i] <= lista_grande_ordenada[i+1]
                           for i in range(len(lista_grande_ordenada)-1))
          else "Incorrecto")

if __name__ == "__main__":
    print("Ejemplos básicos de QuickSort")
    print("============================")
    mostrar_ejemplos()
