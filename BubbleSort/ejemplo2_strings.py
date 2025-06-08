from bubble_sort import bubble_sort
import locale

# Configurar locale para español
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

def ordenar_palabras(palabras):
    # Convertimos la lista a una lista mutable
    lista_palabras = list(palabras)
    # Ordenar usando locale para manejar acentos correctamente
    return bubble_sort(lista_palabras, key=locale.strxfrm)

# Ejemplo de ordenamiento de strings
if __name__ == "__main__":
    # Lista de palabras desordenadas
    palabras = ["zebra", "manzana", "casa", "dado", "árbol"]
    
    print("Lista original de palabras:", palabras)
    
    # Aplicar bubble sort
    palabras_ordenadas = ordenar_palabras(palabras)
    
    print("Lista ordenada de palabras:", palabras_ordenadas)
    
    # Caso con palabras de diferente longitud
    palabras_variadas = ["el", "camino", "a", "la", "programación"]
    print("\nLista original de palabras variadas:", palabras_variadas)
    
    palabras_ordenadas = ordenar_palabras(palabras_variadas)
    print("Lista ordenada de palabras variadas:", palabras_ordenadas)
