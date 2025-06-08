from heap_sort import heapify

def visualizar_heap_sort(arr):
    """
    Implementación visual del HeapSort que muestra cada paso del proceso
    """
    def mostrar_estado(arr, n, i=None, fase="", operacion=""):
        print(f"\n{fase}")
        print(f"Operación: {operacion}")
        print("Estado actual:", arr[:n])
        if i is not None:
            indices = list(range(n))
            marcadores = ["  "] * n
            if i < n:
                marcadores[i] = "↓ "
                # Marcar hijos si existen
                izq = 2 * i + 1
                der = 2 * i + 2
                if izq < n:
                    marcadores[izq] = "← "
                if der < n:
                    marcadores[der] = "→ "
            print("Posición:   ", " ".join(marcadores))
        print("-" * 50)
    
    n = len(arr)
    
    print("Ordenamiento por Montículos (HeapSort)")
    print("=====================================")
    print("\nArray inicial:", arr)
    
    # Fase 1: Construcción del heap
    print("\nFase 1: Construcción del Heap Máximo")
    print("------------------------------------")
    for i in range(n // 2 - 1, -1, -1):
        mostrar_estado(arr, n, i, "Construyendo heap", f"Heapify en índice {i}")
        heapify(arr, n, i)
    
    mostrar_estado(arr, n, None, "Heap máximo construido", "Heap completo")
    
    # Fase 2: Extracción de elementos
    print("\nFase 2: Extracción de Elementos")
    print("-------------------------------")
    for i in range(n-1, 0, -1):
        mostrar_estado(arr, i+1, 0, 
                      "Extracción de elemento", 
                      f"Intercambiar raíz ({arr[0]}) con último elemento ({arr[i]})")
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    print("\nArray ordenado:", arr)
    return arr

if __name__ == "__main__":
    # Lista de ejemplo
    numeros = [12, 11, 13, 5, 6, 7]
    print("Visualización paso a paso de HeapSort")
    lista_ordenada = visualizar_heap_sort(numeros.copy())
