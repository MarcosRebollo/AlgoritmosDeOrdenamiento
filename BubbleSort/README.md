# Ordenamiento Burbuja (Bubble Sort)

## Descripción
El ordenamiento burbuja es un algoritmo de ordenamiento simple que revisa repetidamente cada elemento de la lista para ordenarlos. Funciona comparando elementos adyacentes y los intercambia si están en el orden incorrecto.

## Características
- **Complejidad temporal**: O(n²)
- **Complejidad espacial**: O(1)
- **Es estable**: Sí
- **Es adaptativo**: No

## Funcionamiento
1. Comienza en el primer elemento
2. Compara el elemento actual con el siguiente
3. Si el elemento actual es mayor que el siguiente, los intercambia
4. Avanza a la siguiente posición
5. Repite los pasos 2-4 hasta el final de la lista
6. Repite los pasos 1-5 hasta que no se necesiten más intercambios

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`:
   - Implementación básica con números enteros
   - Manejo de listas con números positivos y negativos
   - Demostración paso a paso del proceso de ordenamiento
   - Verificación de la correctitud del resultado

2. `ejemplo2_strings.py`:
   - Ordenamiento alfabético de cadenas de texto
   - Manejo de palabras de diferentes longitudes
   - Demostración con diferentes tipos de contenido textual
   - Incluye casos con caracteres especiales y mayúsculas/minúsculas

3. `ejemplo3_objetos.py`:
   - Implementación con objetos personalizados
   - Ordenamiento de estructuras de datos complejas
   - Ejemplo con una clase Producto (nombre, precio, cantidad)
   - Demuestra la flexibilidad del algoritmo con diferentes criterios de ordenamiento
