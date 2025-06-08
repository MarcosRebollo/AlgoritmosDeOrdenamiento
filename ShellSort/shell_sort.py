def shell_sort(arr):
    """
    Implementación del algoritmo de ordenamiento Shell
    """
    n = len(arr)
    gap = n // 2
    
    # Comenzar con un gap grande y reducirlo
    while gap > 0:
        # Realizar insertion sort para elementos con el gap actual
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Mover elementos hasta encontrar la posición correcta
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2
    
    return arr
