import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from selection_sort import selection_sort
from BubbleSort.bubble_sort import bubble_sort
from DirectInsertionSort.insertion_sort import insertion_sort
import time
import random
import matplotlib.pyplot as plt

def generar_lista_aleatoria(n):
    return [random.randint(1, 1000) for _ in range(n)]

def medir_tiempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr.copy())
    return time.time() - inicio

def comparar_algoritmos():
    tamaños = [100, 500, 1000, 2000, 3000]
    tiempos_selection = []
    tiempos_insertion = []
    tiempos_bubble = []
    
    for n in tamaños:
        lista = generar_lista_aleatoria(n)
        
        # Medir tiempo para Selection Sort
        tiempo_selection = medir_tiempo(selection_sort, lista)
        tiempos_selection.append(tiempo_selection)
        
        # Medir tiempo para Insertion Sort
        tiempo_insertion = medir_tiempo(insertion_sort, lista)
        tiempos_insertion.append(tiempo_insertion)
        
        # Medir tiempo para Bubble Sort
        tiempo_bubble = medir_tiempo(bubble_sort, lista)
        tiempos_bubble.append(tiempo_bubble)
        
        print(f"\nTamaño de lista: {n}")
        print(f"Selection Sort: {tiempo_selection:.4f} segundos")
        print(f"Insertion Sort: {tiempo_insertion:.4f} segundos")
        print(f"Bubble Sort: {tiempo_bubble:.4f} segundos")
    
    # Crear gráfica de comparación
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_selection, 'o-', label='Selection Sort')
    plt.plot(tamaños, tiempos_insertion, 's-', label='Insertion Sort')
    plt.plot(tamaños, tiempos_bubble, '^-', label='Bubble Sort')
    
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Algoritmos de Ordenamiento')
    plt.legend()
    plt.grid(True)
    
    # Guardar la gráfica
    plt.savefig('comparacion_algoritmos.png')
    print("\nGráfica guardada como 'comparacion_algoritmos.png'")

if __name__ == "__main__":
    print("Comparación de algoritmos de ordenamiento")
    print("========================================")
    
    comparar_algoritmos()
