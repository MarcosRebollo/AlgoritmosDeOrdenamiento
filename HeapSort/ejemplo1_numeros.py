from heap_sort import heap_sort
import random

def imprimir_arbol(arr, n, i, nivel=0):
    """
    Función para imprimir el heap como un árbol
    """
    if i < n:
        espacios = "  " * nivel
        print(f"{espacios}{arr[i]}")
        # Imprimir hijo izquierdo
        imprimir_arbol(arr, n, 2 * i + 1, nivel + 1)
        # Imprimir hijo derecho
        imprimir_arbol(arr, n, 2 * i + 2, nivel + 1)

def mostrar_estado_heap(arr, mensaje):
    """
    Muestra el estado actual del heap como array y como árbol
    """
    print(f"\n{mensaje}")
    print("Array:", arr)
    print("\nEstructura del árbol:")
    imprimir_arbol(arr, len(arr), 0)
    print("-" * 50)

def verificar_ordenamiento(arr):
    """
    Verifica que la lista esté correctamente ordenada
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

if __name__ == "__main__":
    # Probar con diferentes casos
    casos_prueba = [
        [12, 11, 13, 5, 6, 7],  # Caso básico
        [1],  # Un solo elemento
        [],   # Lista vacía
        [4, 4, 4, 4],  # Elementos repetidos
        [5, 4, 3, 2, 1],  # Orden inverso
        [1, 2, 3, 4, 5],  # Ya ordenado
    ]
    
    # Agregar un caso con números aleatorios
    numeros_aleatorios = [random.randint(-1000, 1000) for _ in range(20)]
    casos_prueba.append(numeros_aleatorios)
    
    print("Demostración de HeapSort")
    print("=======================")
    
    for i, caso in enumerate(casos_prueba, 1):
        print(f"\nCaso de prueba {i}:")
        print("Lista original:", caso)
        
        # Crear una copia para no modificar el original
        arr = caso.copy()
        
        # Ordenar
        heap_sort(arr)
        
        # Verificar el resultado
        esta_ordenado = verificar_ordenamiento(arr)
        print("Lista ordenada:", arr)
        print("¿Correctamente ordenado?:", "Sí" if esta_ordenado else "No")
        
        if not esta_ordenado:
            print("¡ERROR! La lista no está correctamente ordenada")
        print("-" * 50)
