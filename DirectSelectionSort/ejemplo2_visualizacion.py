from selection_sort import selection_sort

def mostrar_estado(arr, i, min_idx):
    """Función auxiliar para mostrar el estado del array en cada paso"""
    estado = arr.copy()
    marcadores = ['  '] * len(arr)
    marcadores[i] = '↓ '  # Posición actual
    marcadores[min_idx] = '* '  # Mínimo encontrado
    
    # Mostrar array con marcadores
    print("Array:     ", " ".join(f"{x:2d}" for x in estado))
    print("Posición:  ", " ".join(marcadores))
    print("-" * 40)

def selection_sort_visual(arr):
    """Versión visual del selection sort que muestra el proceso paso a paso"""
    n = len(arr)
    print("Estado inicial:", arr)
    print("\nIniciando ordenamiento por selección:")
    print("=====================================")
    
    for i in range(n):
        min_idx = i
        print(f"\nPaso {i + 1}: Buscando el mínimo desde posición {i}")
        print("(↓ = posición actual, * = mínimo encontrado)")
        mostrar_estado(arr, i, min_idx)
        
        # Buscar el mínimo en el subarreglo no ordenado
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"Nuevo mínimo encontrado en posición {j}:")
                mostrar_estado(arr, i, min_idx)
        
        # Intercambiar elementos
        if min_idx != i:
            print(f"Intercambiando elementos en posiciones {i} y {min_idx}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            mostrar_estado(arr, i, i)
    
    print("\nEstado final:", arr)
    return arr

# Ejemplo de visualización del proceso de ordenamiento
if __name__ == "__main__":
    # Lista desordenada para demostración
    numeros = [64, 34, 25, 12, 22, 11]
    print("Demostración visual del ordenamiento por selección")
    print("================================================")
    
    # Aplicar selection sort con visualización
    lista_ordenada = selection_sort_visual(numeros.copy())
