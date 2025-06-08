from insertion_sort import insertion_sort

def ordenar_palabras(palabras):
    return insertion_sort(list(palabras))

# Ejemplo de ordenamiento de strings
if __name__ == "__main__":
    # Lista de palabras desordenadas
    palabras = ["python", "java", "ruby", "golang", "swift"]
    
    print("Lista original de palabras:", palabras)
    
    # Aplicar insertion sort
    palabras_ordenadas = ordenar_palabras(palabras)
    
    print("Lista ordenada de palabras:", palabras_ordenadas)
    
    # Caso con palabras que empiezan igual
    palabras_similares = ["programar", "programa", "programación", "programador", "programado"]
    print("\nLista de palabras similares:", palabras_similares)
    
    palabras_ordenadas = ordenar_palabras(palabras_similares)
    print("Lista ordenada:", palabras_ordenadas)
    
    # Caso con palabras de diferentes longitudes
    palabras_variadas = ["a", "programa", "de", "computadora", "en", "python"]
    print("\nLista de palabras de diferentes longitudes:", palabras_variadas)
    
    palabras_ordenadas = ordenar_palabras(palabras_variadas)
    print("Lista ordenada:", palabras_ordenadas)
