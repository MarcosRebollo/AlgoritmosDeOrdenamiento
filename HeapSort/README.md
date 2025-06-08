# Ordenamiento por Montículos (HeapSort)

## Descripción
El ordenamiento por montículos es un algoritmo que utiliza una estructura de datos llamada heap (montículo). Un heap es un árbol binario casi completo donde cada nodo padre es mayor (o menor) que sus hijos. HeapSort construye un heap máximo y luego extrae repetidamente el elemento máximo para obtener la secuencia ordenada.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n log n)
  - Caso promedio: O(n log n)
  - Peor caso: O(n log n)
- **Complejidad espacial**: O(1)
- **Es estable**: No
- **Es adaptativo**: No

## Ventajas
- Complejidad garantizada O(n log n) en todos los casos
- Ordenamiento in-place (no requiere memoria adicional)
- Muy eficiente para grandes conjuntos de datos
- Buen rendimiento en memoria virtual

## Desventajas
- No es estable
- No es adaptativo
- Más lento en la práctica que QuickSort para la mayoría de los casos
- Acceso no secuencial a la memoria

## Funcionamiento
1. Fase de construcción del heap:
   - Convertir el array en un heap máximo
   - Comenzar desde el último nodo no hoja
   - Aplicar heapify a cada subárbol
2. Fase de ordenamiento:
   - Intercambiar la raíz con el último elemento
   - Reducir el tamaño del heap
   - Aplicar heapify a la nueva raíz

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`:
   - Implementación básica del HeapSort con números enteros
   - Visualización del proceso de construcción del heap
   - Representación visual del árbol en cada paso
   - Demostración detallada de las fases de construcción y extracción

2. `ejemplo2_rendimiento.py`:
   - Comparación de rendimiento con QuickSort y SelectionSort
   - Medición de tiempos con diferentes tamaños de entrada
   - Generación de gráfica comparativa de rendimiento
   - Análisis detallado de eficiencia con resultados visuales

3. `ejemplo3_visualizacion.py`:
   - Visualización interactiva paso a paso del algoritmo
   - Marcadores visuales para nodos padre e hijos
   - Seguimiento detallado de cada operación de heapify
   - Demostración clara del proceso de intercambio y reestructuración
