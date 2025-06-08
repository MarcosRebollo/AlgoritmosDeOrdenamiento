def selection_sort(arr):
    """
    Implementación del algoritmo de ordenamiento por selección directa
    """
    n = len(arr)
    
    for i in range(n):
        # Encontrar el mínimo elemento en el array desordenado
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambiar el elemento mínimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
