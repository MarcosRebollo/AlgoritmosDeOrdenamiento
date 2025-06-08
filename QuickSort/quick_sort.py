def quick_sort(arr):
    """
    Implementación del algoritmo QuickSort
    """
    if len(arr) <= 1:
        return arr
    
    def partition(low, high):
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
    
    def quick_sort_helper(low, high):
        """
        Función auxiliar recursiva para QuickSort
        """
        if low < high:
            # Encontrar el índice de partición
            pi = partition(low, high)
            
            # Ordenar las mitades izquierda y derecha
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)
    
    quick_sort_helper(0, len(arr) - 1)
    return arr
