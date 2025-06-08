def heapify(arr, n, i):
    """
    Función para mantener la propiedad de heap en un subárbol con raíz en i
    """
    while True:
        mas_grande = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2
        
        # Verifica si el hijo izquierdo es más grande que la raíz
        if izquierda < n and arr[izquierda] > arr[mas_grande]:
            mas_grande = izquierda
        
        # Verifica si el hijo derecho es más grande que el más grande hasta ahora
        if derecha < n and arr[derecha] > arr[mas_grande]:
            mas_grande = derecha
        
        # Si el más grande ya es la raíz, el heap está correcto
        if mas_grande == i:
            break
            
        # Intercambiar y continuar heapifying
        arr[i], arr[mas_grande] = arr[mas_grande], arr[i]
        i = mas_grande

def heap_sort(arr):
    """
    Implementación del algoritmo de ordenamiento por montículos (HeapSort)
    
    Args:
        arr: Lista de elementos comparables a ordenar
        
    Returns:
        Lista ordenada (el mismo objeto, modificado in-place)
    """
    if not arr:
        return arr
        
    n = len(arr)
    
    # Construir un heap máximo (reestructurar el array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraer elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Mover la raíz actual al final
        heapify(arr, i, 0)  # Llamar heapify en el heap reducido
    
    return arr
