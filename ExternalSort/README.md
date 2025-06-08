# Ordenamiento Externo (External Sort)

## Descripción
El ordenamiento externo se utiliza cuando los datos a ordenar son demasiado grandes para caber en la memoria principal (RAM). Este método combina el uso de memoria principal y almacenamiento secundario (disco) para manejar grandes volúmenes de datos.

## Características
- **Complejidad temporal**: O(n log n)
- **Complejidad espacial**: O(1) en memoria principal
- **Espacio en disco**: O(n)
- **Es estable**: Sí (dependiendo de la implementación)
- **Es adaptativo**: Puede serlo (en mezcla natural)

## Ventajas
- Puede manejar volúmenes de datos muy grandes
- Uso eficiente de memoria principal
- Aprovecha secuencias ordenadas existentes
- Escalable a cualquier tamaño de entrada

## Desventajas
- Mayor tiempo de ejecución debido a operaciones E/S
- Requiere espacio adicional en disco
- Complejidad en la implementación
- Rendimiento dependiente del sistema de archivos

## Variantes Implementadas

### 1. Mezcla Directa
- División en bloques de tamaño fijo
- Ordenamiento de cada bloque en memoria
- Mezcla progresiva de bloques ordenados
- Ideal para datos completamente aleatorios

### 2. Mezcla Natural
- Aprovecha secuencias ordenadas existentes
- Detecta y utiliza runs naturales
- Reduce el número de pasadas necesarias
- Más eficiente con datos parcialmente ordenados

### 3. Mezcla Equilibrada
- Distribución balanceada en archivos temporales
- Optimización del uso de buffers
- Control de la fragmentación del disco
- Mejor rendimiento en sistemas con múltiples unidades

## Ejemplos Incluidos

1. `ejemplo1_mezcla_directa.py`:
   - Implementación básica de mezcla directa
   - Ordenamiento con bloques de tamaño fijo
   - Visualización del proceso de división y mezcla
   - Verificación de correctitud del resultado

2. `ejemplo2_mezcla_natural.py`:
   - Detección de secuencias naturales ordenadas
   - Aprovechamiento de orden parcial existente
   - Comparación de eficiencia con diferentes tipos de entrada
   - Demostración de reducción de pasadas

3. `ejemplo3_mezcla_equilibrada.py`:
   - Análisis de rendimiento con diferentes tamaños de bloque
   - Optimización de uso de memoria y disco
   - Medición de tiempos de ejecución
   - Manejo de archivos grandes
