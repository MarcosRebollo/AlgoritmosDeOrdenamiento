def binary_search(arr, val, start, end):
    """
    Implementación de búsqueda binaria para encontrar la posición de inserción
    """
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_insertion_sort(arr):
    """
    Implementación del algoritmo de ordenamiento por inserción binaria
    """
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        
        # Usar búsqueda binaria para encontrar la posición de inserción
        pos = binary_search(arr, val, 0, j)
        
        # Desplazar los elementos mayores que val
        arr[pos+1:i+1] = arr[pos:i]
        arr[pos] = val
    
    return arr
