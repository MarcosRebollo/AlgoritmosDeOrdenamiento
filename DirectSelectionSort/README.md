# Ordenamiento por Selección Directa (Direct Selection Sort)

## Descripción
El ordenamiento por selección directa es un algoritmo que divide la lista en una parte ordenada y otra no ordenada. En cada iteración, busca el elemento más pequeño en la parte no ordenada y lo coloca al final de la parte ordenada.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n²)
  - Caso promedio: O(n²)
  - Peor caso: O(n²)
- **Complejidad espacial**: O(1)
- **Es estable**: No
- **Es adaptativo**: No

## Ventajas
- Simple de implementar
- Número mínimo de intercambios (O(n))
- Funciona bien con elementos grandes y registros pequeños
- Ordenamiento in-place
- Rendimiento predecible

## Desventajas
- No es estable
- No es adaptativo
- Ineficiente para listas grandes
- Siempre realiza O(n²) comparaciones

## Funcionamiento
1. Encontrar el elemento más pequeño de la lista no ordenada
2. Intercambiarlo con el primer elemento de la lista no ordenada
3. Mover el límite de la lista ordenada una posición
4. Repetir hasta ordenar toda la lista

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`:
   - Implementación básica con números enteros
   - Demostración paso a paso del proceso de selección
   - Visualización de las partes ordenada y no ordenada
   - Seguimiento del número de intercambios realizados

2. `ejemplo2_visualizacion.py`:
   - Visualización gráfica del proceso de ordenamiento
   - Representación animada de los intercambios
   - Marcadores para elementos mínimos encontrados
   - Distinción visual entre sección ordenada y no ordenada

3. `ejemplo3_comparacion.py`:
   - Comparación con BubbleSort y DirectInsertionSort
   - Análisis de rendimiento con diferentes tamaños de entrada
   - Medición de número de comparaciones e intercambios
   - Casos de prueba específicos para cada algoritmo
