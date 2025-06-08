# Ordenamiento por Inserción Binaria (Binary Insertion Sort)

## Descripción
El ordenamiento por inserción binaria es una variante optimizada del ordenamiento por inserción directa que utiliza búsqueda binaria para encontrar la posición correcta donde insertar cada elemento. Esto reduce el número de comparaciones necesarias.

## Características
- **Complejidad temporal**: 
  - Mejor caso: O(n log n) para comparaciones, O(n²) para movimientos
  - Caso promedio: O(n log n) para comparaciones, O(n²) para movimientos
  - Peor caso: O(n log n) para comparaciones, O(n²) para movimientos
- **Complejidad espacial**: O(1)
- **Es estable**: Sí
- **Es adaptativo**: No

## Ventajas sobre Inserción Directa
- Reduce significativamente el número de comparaciones
- Más eficiente para listas grandes
- Mantiene la estabilidad del algoritmo original

## Desventajas
- Aún requiere O(n²) operaciones de movimiento
- Más complejo de implementar que la inserción directa
- No mejora significativamente para listas pequeñas

## Funcionamiento
1. Para cada elemento comenzando desde el segundo
2. Usa búsqueda binaria para encontrar la posición correcta en la parte ordenada
3. Desplaza los elementos mayores una posición
4. Inserta el elemento en la posición encontrada

## Ejemplos Incluidos

1. `ejemplo1_numeros.py`: 
   - Ordenamiento básico con números enteros
   - Demuestra el funcionamiento con listas simples
   - Incluye casos con números negativos y duplicados
   - Muestra el antes y después del ordenamiento

2. `ejemplo2_benchmark.py`: 
   - Comparación de rendimiento con el algoritmo de inserción directa
   - Mide tiempos de ejecución con diferentes tamaños de lista
   - Genera gráfica comparativa de rendimiento
   - Muestra las diferencias en tiempo de ejecución

3. `ejemplo3_objetos.py`:
   - Ejemplo avanzado con objetos personalizados (clase Estudiante)
   - Demuestra cómo ordenar objetos por un atributo específico (promedio)
   - Incluye búsqueda binaria para insertar nuevos estudiantes
   - Muestra la versatilidad del algoritmo con tipos de datos complejos
