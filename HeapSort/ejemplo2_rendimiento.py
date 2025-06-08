import os
import sys
import time
import random
import matplotlib.pyplot as plt

# Agregar el directorio padre al path para poder importar los módulos hermanos
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from heap_sort import heap_sort
from QuickSort.quick_sort import quick_sort
from DirectSelectionSort.selection_sort import selection_sort

def generar_lista_aleatoria(n):
    return [random.randint(1, 10000) for _ in range(n)]

def medir_tiempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr.copy())
    return time.time() - inicio

def setup_plot_style():
    """Configura el estilo del plot con o sin seaborn"""
    try:
        plt.style.use('seaborn')
    except:
        # Si seaborn no está disponible, usar un estilo básico pero atractivo
        plt.style.use('default')
        plt.rcParams['axes.grid'] = True
        plt.rcParams['grid.linestyle'] = '--'
        plt.rcParams['grid.alpha'] = 0.7
        plt.rcParams['axes.axisbelow'] = True
        plt.rcParams['figure.figsize'] = [12, 7]

def comparar_rendimiento():
    # Tamaños más variados para mejor comparación
    tamaños = [100, 500, 1000, 2000, 5000, 7500, 10000]
    tiempos_heap = []
    tiempos_quick = []
    tiempos_selection = []
    
    print("Comparación de rendimiento entre algoritmos")
    print("=========================================")
    
    for n in tamaños:
        lista = generar_lista_aleatoria(n)
        
        # Medir HeapSort
        tiempo_heap = medir_tiempo(heap_sort, lista)
        tiempos_heap.append(tiempo_heap)
        
        # Medir QuickSort
        tiempo_quick = medir_tiempo(quick_sort, lista)
        tiempos_quick.append(tiempo_quick)
        
        # Medir SelectionSort
        tiempo_selection = medir_tiempo(selection_sort, lista)
        tiempos_selection.append(tiempo_selection)
        
        print(f"\nTamaño de lista: {n}")
        print(f"HeapSort: {tiempo_heap:.6f} segundos")
        print(f"QuickSort: {tiempo_quick:.6f} segundos")
        print(f"SelectionSort: {tiempo_selection:.6f} segundos")
    
    # Configurar estilo de la gráfica
    setup_plot_style()
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
    
    # Primera gráfica: todos los algoritmos
    ax1.plot(tamaños, tiempos_heap, 'o-', label='HeapSort', linewidth=2, markersize=8)
    ax1.plot(tamaños, tiempos_quick, 's-', label='QuickSort', linewidth=2, markersize=8)
    ax1.plot(tamaños, tiempos_selection, '^-', label='SelectionSort', linewidth=2, markersize=8)
    ax1.set_xlabel('Tamaño de la lista (n)', fontsize=12)
    ax1.set_ylabel('Tiempo (segundos)', fontsize=12)
    ax1.set_title('Comparación de Rendimiento: Todos los Algoritmos', fontsize=14, pad=20)
    ax1.legend(fontsize=10)
    ax1.grid(True, linestyle='--', alpha=0.7)
    
    # Segunda gráfica: solo HeapSort y QuickSort (para mejor visualización)
    ax2.plot(tamaños, tiempos_heap, 'o-', label='HeapSort', linewidth=2, markersize=8)
    ax2.plot(tamaños, tiempos_quick, 's-', label='QuickSort', linewidth=2, markersize=8)
    ax2.set_xlabel('Tamaño de la lista (n)', fontsize=12)
    ax2.set_ylabel('Tiempo (segundos)', fontsize=12)
    ax2.set_title('Comparación Detallada: HeapSort vs QuickSort', fontsize=14, pad=20)
    ax2.legend(fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.7)
    
    # Añadir anotaciones de complejidad
    txt = ('Complejidad teórica:\n'
           'HeapSort: O(n log n)\n'
           'QuickSort: O(n log n)\n'
           'SelectionSort: O(n²)')
    ax1.text(0.02, 0.98, txt, transform=ax1.transAxes, 
             bbox=dict(facecolor='white', alpha=0.8),
             fontsize=10, verticalalignment='top')
    
    # Ajustar márgenes y guardar
    plt.tight_layout()
    plt.savefig('comparacion_rendimiento.png', dpi=300, bbox_inches='tight')
    print("\nGráfica guardada como 'comparacion_rendimiento.png'")
    
    # Mostrar estadísticas comparativas
    print("\nEstadísticas comparativas:")
    print("-------------------------")
    for i, n in enumerate(tamaños):
        print(f"\nTamaño {n}:")
        print(f"HeapSort vs QuickSort: {tiempos_heap[i]/tiempos_quick[i]:.2f}x")
        if tiempos_selection[i] > 0:  # Evitar división por cero
            print(f"HeapSort vs SelectionSort: {tiempos_heap[i]/tiempos_selection[i]:.2f}x")
            print(f"QuickSort vs SelectionSort: {tiempos_quick[i]/tiempos_selection[i]:.2f}x")

if __name__ == "__main__":
    comparar_rendimiento()
