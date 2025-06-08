def shell_sort_custom_gaps(arr, gap_sequence):
    """
    Implementación de Shell Sort que permite especificar la secuencia de gaps
    """
    n = len(arr)
    
    # Encontrar el primer gap válido (menor que n)
    gap_idx = 0
    while gap_idx < len(gap_sequence) and gap_sequence[gap_idx] >= n:
        gap_idx += 1
    
    # Ordenar con cada gap
    while gap_idx < len(gap_sequence):
        gap = gap_sequence[gap_idx]
        
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
            
        gap_idx += 1
    
    return arr

def mostrar_proceso_gap(arr, gap, mensaje):
    """Muestra el estado del array después de aplicar un gap"""
    print(f"\n{mensaje} (gap = {gap}):")
    print("Array:", arr)
    
    # Mostrar las sublistas formadas por el gap
    for inicio in range(gap):
        sublista = arr[inicio::gap]
        if sublista:
            print(f"Sublista {inicio + 1}: {sublista}")

if __name__ == "__main__":
    # Lista de prueba
    numeros = [64, 34, 25, 12, 22, 11, 90, 45, 33, 21, 10, 5]
    print("Lista original:", numeros)
    
    # Probar diferentes secuencias de gaps
    
    # 1. Secuencia original de Shell (N/2, N/4, ..., 1)
    print("\n=== Secuencia original de Shell ===")
    n = len(numeros)
    gaps_shell = []
    gap = n // 2
    while gap > 0:
        gaps_shell.append(gap)
        gap //= 2
    
    resultado = shell_sort_custom_gaps(numeros.copy(), gaps_shell)
    print("Secuencia de gaps:", gaps_shell)
    print("Resultado:", resultado)
    
    # 2. Secuencia de Hibbard (2^k - 1)
    print("\n=== Secuencia de Hibbard ===")
    gaps_hibbard = []
    k = 1
    while True:
        gap = 2**k - 1
        if gap >= n:
            break
        gaps_hibbard.append(gap)
        k += 1
    gaps_hibbard.reverse()
    
    resultado = shell_sort_custom_gaps(numeros.copy(), gaps_hibbard)
    print("Secuencia de gaps:", gaps_hibbard)
    print("Resultado:", resultado)
    
    # 3. Secuencia de Knuth (3^k - 1)
    print("\n=== Secuencia de Knuth ===")
    gaps_knuth = []
    k = 1
    while True:
        gap = (3**k - 1) // 2
        if gap >= n:
            break
        gaps_knuth.append(gap)
        k += 1
    gaps_knuth.reverse()
    
    resultado = shell_sort_custom_gaps(numeros.copy(), gaps_knuth)
    print("Secuencia de gaps:", gaps_knuth)
    print("Resultado:", resultado)
