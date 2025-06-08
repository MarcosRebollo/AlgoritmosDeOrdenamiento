# Ordenamiento Rápido (QuickSort)

## Descripción
QuickSort es un algoritmo de ordenamiento eficiente que utiliza la estrategia "divide y vencerás". Funciona seleccionando un elemento como pivote y particionando el array alrededor del pivote, de manera que los elementos menores queden a la izquierda y los mayores a la derecha.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n log n)
  - Caso promedio: O(n log n)
  - Peor caso: O(n²)
- **Complejidad espacial**: O(log n)
- **Es estable**: No
- **Es adaptativo**: No

## Ventajas
- Muy eficiente en la práctica
- Bajo uso de memoria
- Buen rendimiento con la caché del procesador
- Se puede implementar de forma que use poco espacio adicional

## Desventajas
- No es estable
- El peor caso es O(n²)
- Sensible a la elección del pivote
- No es adaptativo

## Variantes de Implementación
1. Elección del pivote:
   - Último elemento
   - Primer elemento
   - Elemento aleatorio
   - Mediana de tres
2. Partición:
   - Esquema de Lomuto
   - Esquema de Hoare
   - Partición de tres vías

## Ejemplos Incluidos

1. `ejemplo1_basico.py`:
   - Implementación básica del algoritmo con varios tipos de datos
   - Ordenamiento de números enteros, flotantes y strings
   - Demostración con listas de diferentes tamaños
   - Verificación de correctitud del ordenamiento

2. `ejemplo2_pivotes.py`:
   - Comparación de diferentes estrategias de selección de pivote
   - Implementación de pivote último, aleatorio y mediana de tres
   - Análisis de rendimiento con diferentes tipos de entrada
   - Demostración con casos especiales (listas casi ordenadas)

3. `ejemplo3_visualizacion.py`:
   - Visualización paso a paso del proceso de partición
   - Seguimiento del pivote y subparticiones en cada nivel
   - Representación visual del estado del array en cada paso
   - Demostración clara del proceso recursivo
