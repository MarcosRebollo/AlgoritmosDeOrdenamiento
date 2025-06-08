# Ordenamiento Shell (Shell Sort)

## Descripción
El ordenamiento Shell es una mejora del algoritmo de inserción directa que permite el intercambio de elementos distantes. El algoritmo divide la lista en sublistas más pequeñas que se ordenan usando inserción directa, y progresivamente reduce el tamaño de las sublistas hasta ordenar la lista completa.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n log n)
  - Caso promedio: Depende de la secuencia de gaps, generalmente O(n log² n)
  - Peor caso: O(n²)
- **Complejidad espacial**: O(1)
- **Es estable**: No
- **Es adaptativo**: Sí

## Ventajas
- Más eficiente que el algoritmo de inserción para listas grandes
- Requiere menos operaciones que otros algoritmos O(n²)
- Funciona muy bien para listas parcialmente ordenadas
- Usa memoria in-place

## Desventajas
- La complejidad depende de la secuencia de gaps elegida
- No es estable
- Más complejo de implementar que inserción directa
- El rendimiento puede variar significativamente según la entrada

## Funcionamiento
1. Se define una secuencia de gaps (intervalos)
2. Para cada gap:
   - Se divide la lista en sublistas de elementos separados por el gap
   - Se ordena cada sublista usando inserción directa
   - Se reduce el gap y se repite el proceso
3. El último gap siempre es 1, realizando una inserción directa final

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`:
   - Implementación básica con diferentes tamaños de lista
   - Ordenamiento de listas pequeñas, medianas y grandes
   - Generación de casos de prueba aleatorios
   - Verificación automática de la correctitud del ordenamiento

2. `ejemplo2_gaps.py`:
   - Demostración de diferentes secuencias de gaps
   - Implementación de secuencia original de Shell (N/2)
   - Implementación de secuencia de Hibbard (2^k - 1)
   - Implementación de secuencia de Knuth (3^k - 1)
   - Comparación de rendimiento entre diferentes secuencias

3. `ejemplo3_visualizacion.py`:
   - Visualización detallada del proceso de ordenamiento
   - Representación del estado del array en cada paso
   - Seguimiento de comparaciones e intercambios
   - Marcadores visuales para las posiciones activas y gaps
