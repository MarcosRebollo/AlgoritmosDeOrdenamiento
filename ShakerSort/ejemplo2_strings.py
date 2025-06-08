from shaker_sort import shaker_sort

def ordenar_palabras(palabras):
    return shaker_sort(list(palabras))

# Ejemplo de ordenamiento de strings
if __name__ == "__main__":
    # Lista de palabras desordenadas
    palabras = ["zebra", "manzana", "casa", "dado", "árbol"]
    
    print("Lista original de palabras:", palabras)
    
    # Aplicar shaker sort
    palabras_ordenadas = ordenar_palabras(palabras)
    
    print("Lista ordenada de palabras:", palabras_ordenadas)
    
    # Caso con palabras largas y cortas mezcladas
    palabras_mixtas = ["a", "programación", "b", "desarrollo", "c", "python"]
    print("\nLista de palabras mixtas:", palabras_mixtas)
    
    palabras_ordenadas = ordenar_palabras(palabras_mixtas)
    print("Lista ordenada:", palabras_ordenadas)
