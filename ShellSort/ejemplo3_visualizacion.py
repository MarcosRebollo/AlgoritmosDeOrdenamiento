def shell_sort_visual(arr):
    """
    Implementación visual del algoritmo Shell Sort que muestra el proceso paso a paso
    """
    def mostrar_estado(arr, gap, i, j, temp):
        estado = arr.copy()
        marcadores = ['  '] * len(arr)
        if j >= 0:
            marcadores[j] = '← '  # Posición actual
            if j + gap < len(arr):
                marcadores[j + gap] = '→ '  # Elemento comparado
        print(f"\nGap = {gap}")
        print("Array:    ", " ".join(f"{x:2d}" for x in estado))
        print("Posición: ", " ".join(marcadores))
        print("Temporal: ", temp)
        print("-" * 50)
    
    n = len(arr)
    gap = n // 2
    
    print("Estado inicial:", arr)
    print("\nIniciando ordenamiento Shell:")
    print("============================")
    
    while gap > 0:
        print(f"\nNueva iteración con gap = {gap}")
        print("-----------------------------")
        
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            mostrar_estado(arr, gap, i, j, temp)
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                mostrar_estado(arr, gap, i, j, temp)
            
            arr[j] = temp
            if j != i:
                print(f"Colocando {temp} en la posición {j}")
                mostrar_estado(arr, gap, i, j, temp)
        
        gap //= 2
    
    print("\nEstado final:", arr)
    return arr

# Ejemplo de visualización del proceso de ordenamiento
if __name__ == "__main__":
    # Lista desordenada para demostración
    numeros = [64, 34, 25, 12, 22, 11]
    print("Demostración visual del ordenamiento Shell")
    print("=========================================")
    
    # Aplicar shell sort con visualización
    lista_ordenada = shell_sort_visual(numeros.copy())
