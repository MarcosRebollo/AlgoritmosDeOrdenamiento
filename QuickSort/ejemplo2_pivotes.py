import random

def quick_sort_ultimo(arr):
    """QuickSort usando el último elemento como pivote"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    menores = [x for x in arr[:-1] if x <= pivot]
    mayores = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort_ultimo(menores) + [pivot] + quick_sort_ultimo(mayores)

def quick_sort_primero(arr):
    """QuickSort usando el primer elemento como pivote"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    menores = [x for x in arr[1:] if x <= pivot]
    mayores = [x for x in arr[1:] if x > pivot]
    
    return quick_sort_primero(menores) + [pivot] + quick_sort_primero(mayores)

def quick_sort_aleatorio(arr):
    """QuickSort usando un elemento aleatorio como pivote"""
    if len(arr) <= 1:
        return arr
    
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    menores = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_idx]
    mayores = [x for i, x in enumerate(arr) if x > pivot and i != pivot_idx]
    
    return quick_sort_aleatorio(menores) + [pivot] + quick_sort_aleatorio(mayores)

def quick_sort_mediana(arr):
    """QuickSort usando la mediana de tres como pivote"""
    if len(arr) <= 1:
        return arr
    
    # Seleccionar la mediana de tres elementos
    inicio, medio, fin = 0, len(arr)//2, len(arr)-1
    pivot_idx = sorted([(arr[inicio], inicio), 
                       (arr[medio], medio), 
                       (arr[fin], fin)], 
                      key=lambda x: x[0])[1][1]
    
    pivot = arr[pivot_idx]
    menores = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_idx]
    mayores = [x for i, x in enumerate(arr) if x > pivot and i != pivot_idx]
    
    return quick_sort_mediana(menores) + [pivot] + quick_sort_mediana(mayores)

if __name__ == "__main__":
    # Lista de prueba
    numeros = [64, 34, 25, 12, 22, 11, 90, 45, 33, 21, 10, 5]
    print("Lista original:", numeros)
    
    # Probar diferentes estrategias de pivote
    print("\nÚltimo elemento como pivote:")
    resultado = quick_sort_ultimo(numeros.copy())
    print("Resultado:", resultado)
    
    print("\nPrimer elemento como pivote:")
    resultado = quick_sort_primero(numeros.copy())
    print("Resultado:", resultado)
    
    print("\nElemento aleatorio como pivote:")
    resultado = quick_sort_aleatorio(numeros.copy())
    print("Resultado:", resultado)
    
    print("\nMediana de tres como pivote:")
    resultado = quick_sort_mediana(numeros.copy())
    print("Resultado:", resultado)
    
    # Prueba con caso especial (lista casi ordenada)
    casi_ordenada = [1, 2, 3, 5, 4, 6, 7, 8]
    print("\nPrueba con lista casi ordenada:", casi_ordenada)
    
    print("\nÚltimo elemento como pivote:")
    resultado = quick_sort_ultimo(casi_ordenada.copy())
    print("Resultado:", resultado)
    
    print("\nMediana de tres como pivote:")
    resultado = quick_sort_mediana(casi_ordenada.copy())
    print("Resultado:", resultado)
