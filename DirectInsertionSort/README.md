# Ordenamiento por Inserción Directa (Direct Insertion Sort)

## Descripción
El ordenamiento por inserción directa es un algoritmo simple que construye la lista ordenada final insertando un elemento a la vez. Es similar a cómo las personas ordenan cartas en su mano: se toma una carta y se inserta en su posición correcta entre las cartas ya ordenadas.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n)
  - Caso promedio: O(n²)
  - Peor caso: O(n²)
- **Complejidad espacial**: O(1)
- **Es estable**: Sí
- **Es adaptativo**: Sí

## Ventajas
- Simple de implementar
- Eficiente para conjuntos pequeños de datos
- Adaptativo: eficiente para datos parcialmente ordenados
- Estable: mantiene el orden relativo de elementos iguales
- Ordenamiento in-place
- Online: puede ordenar los datos conforme llegan

## Funcionamiento
1. Comenzar con el segundo elemento
2. Comparar con los elementos anteriores
3. Desplazar elementos mayores una posición
4. Insertar el elemento en la posición correcta
5. Repetir hasta procesar todos los elementos

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`:
   - Implementación básica con números enteros
   - Visualización paso a paso del proceso de inserción
   - Demostración con diferentes tipos de secuencias numéricas
   - Casos de prueba con listas ordenadas, inversas y aleatorias

2. `ejemplo2_strings.py`:
   - Ordenamiento alfabético de cadenas de texto
   - Manejo de mayúsculas, minúsculas y caracteres especiales
   - Implementación con comparación personalizada de strings
   - Ejemplos con diferentes longitudes de palabras

3. `ejemplo3_tiempo_real.py`:
   - Demostración de inserción en tiempo real
   - Simulación de llegada de datos en streaming
   - Mantenimiento de una lista ordenada con inserciones dinámicas
   - Visualización del proceso de inserción en tiempo real
