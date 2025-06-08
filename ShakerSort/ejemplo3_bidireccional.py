from shaker_sort import shaker_sort

def mostrar_proceso(arr, i, direccion):
    """Función auxiliar para mostrar el proceso de ordenamiento"""
    estado = arr.copy()
    if direccion == "forward":
        estado.insert(i, "→")
    else:
        estado.insert(i + 1, "←")
    print(" ".join(str(x) for x in estado))

def shaker_sort_visual(arr):
    """Versión visual del shaker sort que muestra el proceso bidireccional"""
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    print("Estado inicial:", arr)
    print("\nIniciando ordenamiento bidireccional:")
    
    while swapped:
        swapped = False
        
        print("\nMovimiento de izquierda a derecha:")
        # Forward pass
        for i in range(start, end):
            mostrar_proceso(arr, i, "forward")
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        end = end - 1
        swapped = False
        
        print("\nMovimiento de derecha a izquierda:")
        # Backward pass
        for i in range(end - 1, start - 1, -1):
            mostrar_proceso(arr, i, "backward")
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start = start + 1
    
    print("\nEstado final:", arr)
    return arr

# Ejemplo de visualización del proceso bidireccional
if __name__ == "__main__":
    # Lista desordenada para demostración
    numeros = [6, 4, 2, 8, 1, 5]
    print("Demostración visual del ordenamiento por sacudida")
    print("------------------------------------------------")
    
    # Aplicar shaker sort con visualización
    lista_ordenada = shaker_sort_visual(numeros.copy())
    
    # Demostración con una lista más grande
    print("\n\nDemostración con una lista más grande:")
    lista_grande = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    lista_ordenada = shaker_sort_visual(lista_grande.copy())
