def insertion_sort(arr):
    """
    Implementación del algoritmo de ordenamiento por inserción directa
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Mover elementos que son mayores que key
        # a una posición adelante de su posición actual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr
