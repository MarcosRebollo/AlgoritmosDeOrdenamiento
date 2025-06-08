def bubble_sort(arr, key=None):
    n = len(arr)
    # Si no se proporciona función key, usar la identidad
    if key is None:
        key = lambda x: x
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparar elementos adyacentes usando la función key
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
