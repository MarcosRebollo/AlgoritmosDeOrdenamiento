import os
import sys

# Agregar el directorio padre al path para poder importar los módulos hermanos
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

def partition(arr, low, high):
    """
    Función de partición que toma el último elemento como pivote,
    lo coloca en su posición correcta y coloca los elementos menores
    a la izquierda y los mayores a la derecha
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def visualizar_quicksort(arr):
    """
    Implementación visual de QuickSort que muestra el proceso paso a paso
    """
    def mostrar_estado(arr, low, high, pivot_idx=None, mensaje=""):
        print(f"\n{mensaje}")
        for i in range(len(arr)):
            if i == pivot_idx:
                print("P", end=" ")
            elif low <= i <= high:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
        print(" ".join(map(str, arr)))
        print("-" * 50)
    
    def quicksort_visual(arr, low, high, nivel=0):
        if low < high:
            # Mostrar el subarreglo actual
            indent = "  " * nivel
            print(f"\n{indent}Nivel {nivel}: Ordenando subarreglo[{low}:{high+1}]")
            mostrar_estado(arr, low, high)
            
            # Encontrar el índice de partición
            pivot_idx = high
            mostrar_estado(arr, low, high, pivot_idx, 
                         f"{indent}Pivote seleccionado: {arr[pivot_idx]}")
            
            # Particionar el arreglo
            pi = partition(arr, low, high)
            mostrar_estado(arr, low, high, pi, 
                         f"{indent}Después de particionar (pivote en posición {pi})")
            
            # Ordenar recursivamente las subpartes
            print(f"{indent}Ordenando lado izquierdo...")
            quicksort_visual(arr, low, pi - 1, nivel + 1)
            print(f"{indent}Ordenando lado derecho...")
            quicksort_visual(arr, pi + 1, high, nivel + 1)
    
    print("Visualización paso a paso de QuickSort")
    print("====================================")
    quicksort_visual(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    # Lista de ejemplo
    numeros = [64, 34, 25, 12, 22, 11]
    print("Lista original:", numeros)
    
    # Aplicar quicksort con visualización
    lista_ordenada = visualizar_quicksort(numeros.copy())
    print("\nLista ordenada final:", lista_ordenada)
    
    # Ejemplo con lista más pequeña para mejor visualización
    print("\n\nEjemplo con lista más pequeña:")
    numeros_pequeños = [3, 1, 4, 2]
    lista_ordenada = visualizar_quicksort(numeros_pequeños.copy())
