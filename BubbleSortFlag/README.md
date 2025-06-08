# Ordenamiento Burbuja con Señal (Bubble Sort with Flag)

## Descripción
El ordenamiento burbuja con señal es una mejora del algoritmo de burbuja básico. La diferencia principal es que utiliza una variable booleana (señal) para detectar si se realizó algún intercambio durante una pasada. Si no hubo intercambios, significa que la lista ya está ordenada y el algoritmo puede terminar antes.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n) cuando la lista ya está ordenada
  - Caso promedio: O(n²)
  - Peor caso: O(n²)
- **Complejidad espacial**: O(1)
- **Es estable**: Sí
- **Es adaptativo**: Sí

## Ventajas sobre Bubble Sort básico
- Detecta cuando la lista ya está ordenada y termina antes
- Más eficiente para listas parcialmente ordenadas
- Reduce el número de iteraciones innecesarias

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`:
   - Ordenamiento básico usando la bandera de optimización
   - Demostración con diferentes tamaños de listas
   - Manejo de casos con listas casi ordenadas
   - Comparación de iteraciones necesarias vs bubble sort básico

2. `ejemplo2_strings.py`:
   - Ordenamiento de cadenas de texto con detección temprana
   - Manejo de diferentes tipos de strings (cortos, largos, especiales)
   - Demostración de la eficiencia con listas parcialmente ordenadas
   - Incluye casos con strings similares y diferentes

3. `ejemplo3_rendimiento.py`:
   - Análisis detallado del rendimiento del algoritmo
   - Medición de tiempos con diferentes tamaños de entrada
   - Comparación de casos mejor y peor
   - Visualización de la mejora respecto a la versión básica
