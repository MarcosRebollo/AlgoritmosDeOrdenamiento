import os
import tempfile
import random
import shutil

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def crear_archivo_datos(nombre_archivo, cantidad):
    """
    Crea un archivo con secuencias parcialmente ordenadas
    """
    ruta_completa = os.path.join(SCRIPT_DIR, nombre_archivo)
    with open(ruta_completa, 'w') as f:
        # Crear secuencias ordenadas con algunos desórdenes
        secuencia_actual = []
        for _ in range(cantidad):
            if not secuencia_actual or random.random() < 0.2:  # 20% de probabilidad de nueva secuencia
                secuencia_actual = []
                base = random.randint(1, 1000)
                for i in range(random.randint(5, 15)):  # Secuencias de 5-15 números
                    secuencia_actual.append(base + i)
            
            # Agregar número de la secuencia con posible desorden
            if random.random() < 0.1:  # 10% de probabilidad de desorden
                f.write(f"{random.randint(1, 10000)}\n")
            else:
                f.write(f"{secuencia_actual.pop(0)}\n")
                if not secuencia_actual:
                    base = random.randint(1, 1000)
                    for i in range(random.randint(5, 15)):
                        secuencia_actual.append(base + i)

def encontrar_secuencias_naturales(archivo):
    """
    Encuentra secuencias naturalmente ordenadas en el archivo
    Retorna una lista de tuplas (inicio, fin) de cada secuencia
    """
    ruta_completa = os.path.join(SCRIPT_DIR, archivo) if not os.path.isabs(archivo) else archivo
    secuencias = []
    inicio_actual = 0
    numero_anterior = None
    
    with open(ruta_completa, 'r') as f:
        for i, linea in enumerate(f):
            numero_actual = int(linea)
            if numero_anterior is not None and numero_actual < numero_anterior:
                secuencias.append((inicio_actual, i))
                inicio_actual = i
            numero_anterior = numero_actual
    
    # Agregar la última secuencia
    secuencias.append((inicio_actual, i + 1))
    return secuencias

def mezclar_secuencias(archivo_entrada, secuencia1, secuencia2, archivo_salida):
    """Mezcla dos secuencias ordenadas de un archivo"""
    ruta_entrada = os.path.join(SCRIPT_DIR, archivo_entrada) if not os.path.isabs(archivo_entrada) else archivo_entrada
    ruta_salida = os.path.join(SCRIPT_DIR, archivo_salida) if not os.path.isabs(archivo_salida) else archivo_salida
    
    with open(ruta_entrada, 'r') as entrada, open(ruta_salida, 'w') as salida:
        # Posicionar en inicio de primera secuencia
        entrada.seek(0)
        for _ in range(secuencia1[0]):
            entrada.readline()
            
        # Leer primera secuencia
        nums1 = [int(entrada.readline()) for _ in range(secuencia1[1] - secuencia1[0])]
        
        # Posicionar en inicio de segunda secuencia
        entrada.seek(0)
        for _ in range(secuencia2[0]):
            entrada.readline()
            
        # Leer segunda secuencia
        nums2 = [int(entrada.readline()) for _ in range(secuencia2[1] - secuencia2[0])]
        
        # Mezclar secuencias
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                salida.write(f"{nums1[i]}\n")
                i += 1
            else:
                salida.write(f"{nums2[j]}\n")
                j += 1
        
        # Escribir números restantes
        while i < len(nums1):
            salida.write(f"{nums1[i]}\n")
            i += 1
        while j < len(nums2):
            salida.write(f"{nums2[j]}\n")
            j += 1

def mezcla_natural(archivo_entrada, archivo_salida):
    """Implementación del ordenamiento por mezcla natural"""
    # Ensure absolute paths
    ruta_entrada = os.path.join(SCRIPT_DIR, archivo_entrada) if not os.path.isabs(archivo_entrada) else archivo_entrada
    ruta_salida = os.path.join(SCRIPT_DIR, archivo_salida) if not os.path.isabs(archivo_salida) else archivo_salida
    archivo_actual = ruta_entrada
    
    # Create temporary files in the script directory
    temp_count = 1
    archivo_temp = os.path.join(SCRIPT_DIR, f'temp_natural_{temp_count}.txt')
    
    try:
        while True:
            # Encontrar secuencias naturales
            secuencias = encontrar_secuencias_naturales(archivo_actual)
            
            # Si solo hay una secuencia, el archivo está ordenado
            if len(secuencias) == 1:
                if archivo_actual != ruta_salida:
                    shutil.copy2(archivo_actual, ruta_salida)
                break
            
            # Mezclar secuencias de dos en dos
            temp_count += 1
            archivo_temp_nuevo = os.path.join(SCRIPT_DIR, f'temp_natural_{temp_count}.txt')
            
            for i in range(0, len(secuencias) - 1, 2):
                mezclar_secuencias(archivo_actual, secuencias[i], secuencias[i + 1], archivo_temp_nuevo)
            
            # Intercambiar archivos para la siguiente iteración
            if archivo_actual != ruta_entrada and os.path.exists(archivo_actual):
                os.unlink(archivo_actual)
            archivo_actual = archivo_temp_nuevo
            archivo_temp = os.path.join(SCRIPT_DIR, f'temp_natural_{temp_count + 1}.txt')
    finally:
        # Cleanup temporary files
        for i in range(1, temp_count + 2):
            temp_file = os.path.join(SCRIPT_DIR, f'temp_natural_{i}.txt')
            if os.path.exists(temp_file) and temp_file != ruta_salida:
                try:
                    os.unlink(temp_file)
                except:
                    pass

if __name__ == "__main__":
    # Usar rutas relativas dentro de la carpeta ExternalSort
    directorio = os.path.dirname(__file__)
    entrada = os.path.join(directorio, "datos_secuenciales.txt")
    salida = os.path.join(directorio, "datos_ordenados.txt")
    
    print("Demostración de Ordenamiento Externo - Mezcla Natural")
    print("==================================================")
    
    # Crear archivo con secuencias parcialmente ordenadas
    print("\nCreando archivo con secuencias parcialmente ordenadas...")
    with open(entrada, 'w') as f:
        # Crear varias secuencias ordenadas con algunos desajustes
        for i in range(5):
            base = i * 100
            numeros = sorted(random.randint(base, base + 99) for _ in range(20))
            for num in numeros:
                f.write(f"{num}\n")
    
    # Mostrar secuencias naturales encontradas
    print("\nSecuencias naturales en el archivo original:")
    secuencias = encontrar_secuencias_naturales(entrada)
    print(f"Número de secuencias: {len(secuencias)}")
    
    # Ordenar archivo
    print("\nOrdenando archivo...")
    mezcla_natural(entrada, salida)
    
    # Verificar resultado
    print("\nVerificando ordenamiento...")
    numeros = []
    with open(salida, 'r') as f:
        numeros = [int(linea) for linea in f]
    
    ordenado = all(numeros[i] <= numeros[i+1] for i in range(len(numeros)-1))
    print(f"Ordenamiento {'correcto' if ordenado else 'incorrecto'}")
    print(f"Primeros 10 números ordenados: {numeros[:10]}")
    
    # Limpiar archivos
    os.unlink(entrada)
    os.unlink(salida)
