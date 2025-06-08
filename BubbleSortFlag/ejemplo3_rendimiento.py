from bubble_sort_flag import bubble_sort_flag
import time
import random

def generar_lista_aleatoria(n):
    return [random.randint(1, 1000) for _ in range(n)]

def generar_lista_casi_ordenada(n):
    lista = list(range(n))
    # Desordenar solo el 10% de los elementos
    for _ in range(n // 10):
        i = random.randint(0, n-2)
        lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def medir_tiempo(func, lista):
    inicio = time.time()
    func(lista.copy())
    fin = time.time()
    return fin - inicio

# Ejemplo de comparación de rendimiento
if __name__ == "__main__":
    # Prueba con diferentes tamaños de lista
    tamaños = [100, 500, 1000]
    
    print("Comparación de rendimiento con listas aleatorias:")
    print("------------------------------------------------")
    for n in tamaños:
        lista_aleatoria = generar_lista_aleatoria(n)
        tiempo = medir_tiempo(bubble_sort_flag, lista_aleatoria)
        print(f"Tamaño {n}: {tiempo:.4f} segundos")
    
    print("\nComparación de rendimiento con listas casi ordenadas:")
    print("----------------------------------------------------")
    for n in tamaños:
        lista_casi_ordenada = generar_lista_casi_ordenada(n)
        tiempo = medir_tiempo(bubble_sort_flag, lista_casi_ordenada)
        print(f"Tamaño {n}: {tiempo:.4f} segundos")
