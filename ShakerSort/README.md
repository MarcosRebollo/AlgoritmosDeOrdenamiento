# Ordenamiento por Sacudida (Shaker Sort)

## Descripción
El ordenamiento por sacudida, también conocido como cocktail sort, es una variación del ordenamiento burbuja que opera en ambas direcciones. Mientras que el bubble sort solo atraviesa la lista de izquierda a derecha, el shaker sort va en ambas direcciones: de izquierda a derecha y luego de derecha a izquierda.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n) cuando la lista ya está ordenada
  - Caso promedio: O(n²)
  - Peor caso: O(n²)
- **Complejidad espacial**: O(1)
- **Es estable**: Sí
- **Es adaptativo**: Sí

## Ventajas
- Más eficiente que el bubble sort para algunos casos
- Resuelve el problema de las "tortugas" (elementos pequeños al final de la lista)
- Mejor rendimiento con listas parcialmente ordenadas
- Detecta tempranamente si la lista está ordenada

## Desventajas
- Mantiene la complejidad O(n²) del bubble sort
- Realiza más operaciones por iteración
- No es eficiente para listas grandes
- Mayor complejidad de implementación que bubble sort

## Funcionamiento
1. Realiza un recorrido de izquierda a derecha (como bubble sort)
2. Luego realiza un recorrido de derecha a izquierda
3. En cada pasada se van fijando los elementos más grandes y más pequeños
4. El proceso continúa hasta que no se realicen más intercambios

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`:
   - Ordenamiento básico con números enteros
   - Demostración con listas de diferentes tamaños
   - Caso especial con "tortugas" (números pequeños al final)
   - Verificación de la efectividad del algoritmo

2. `ejemplo2_strings.py`:
   - Ordenamiento de cadenas de texto
   - Manejo de diferentes longitudes de palabras
   - Comparación de caracteres especiales
   - Demostración de la estabilidad del algoritmo

3. `ejemplo3_bidireccional.py`:
   - Visualización del proceso bidireccional
   - Seguimiento de los movimientos en ambas direcciones
   - Demostración del progreso paso a paso
   - Comparación con el proceso unidireccional del bubble sort
