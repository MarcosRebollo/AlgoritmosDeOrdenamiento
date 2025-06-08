import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from binary_insertion_sort import binary_insertion_sort
from DirectInsertionSort.insertion_sort import insertion_sort
import time
import random
import matplotlib.pyplot as plt

def generar_lista_aleatoria(n):
    return [random.randint(1, 10000) for _ in range(n)]

def medir_tiempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr.copy())
    return time.time() - inicio

def comparar_rendimiento():
    tamaños = [100, 500, 1000, 2000, 3000, 4000, 5000]
    tiempos_binario = []
    tiempos_normal = []
    
    print("Comparando rendimiento de Inserción Binaria vs Inserción Directa")
    print("============================================================")
    
    for n in tamaños:
        lista = generar_lista_aleatoria(n)
        
        # Medir tiempo para inserción binaria
        tiempo_binario = medir_tiempo(binary_insertion_sort, lista)
        tiempos_binario.append(tiempo_binario)
        
        # Medir tiempo para inserción directa
        tiempo_normal = medir_tiempo(insertion_sort, lista)
        tiempos_normal.append(tiempo_normal)
        
        print(f"\nTamaño de lista: {n}")
        print(f"Inserción Binaria: {tiempo_binario:.6f} segundos")
        print(f"Inserción Directa: {tiempo_normal:.6f} segundos")
        print(f"Diferencia: {abs(tiempo_normal - tiempo_binario):.6f} segundos")
    
    # Crear gráfica comparativa
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_binario, 'o-', label='Inserción Binaria')
    plt.plot(tamaños, tiempos_normal, 's-', label='Inserción Directa')
    
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación: Inserción Binaria vs Inserción Directa')
    plt.legend()
    plt.grid(True)
    
    # Guardar gráfica
    plt.savefig('comparacion_insercion.png')
    print("\nGráfica guardada como 'comparacion_insercion.png'")

if __name__ == "__main__":
    comparar_rendimiento()
