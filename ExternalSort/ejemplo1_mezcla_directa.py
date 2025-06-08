from external_sort import ExternalSort
import random
import os
import traceback

class MezclaDirecta(ExternalSort):
    def __init__(self):
        super().__init__()

    def ordenar_bloque(self, numeros):
        """Ordena un bloque de números en memoria"""
        return sorted([float(num.strip()) for num in numeros])
    
    def mezcla_directa(self, archivo_entrada, archivo_salida, tamaño_bloque=100):
        """Implementación del ordenamiento por mezcla directa con tamaño de bloque"""
        ruta_entrada = self._ensure_absolute_path(archivo_entrada)
        ruta_salida = self._ensure_absolute_path(archivo_salida)
        bloques_temp = []
        
        try:
            # Leer y ordenar bloques
            with open(ruta_entrada, 'r') as entrada:
                while True:
                    # Leer un bloque
                    bloque = []
                    for _ in range(tamaño_bloque):
                        linea = entrada.readline().strip()
                        if not linea:
                            break
                        try:
                            # Verificar que podemos convertir a float
                            float(linea)
                            bloque.append(linea)
                        except ValueError as e:
                            print(f"Error al convertir línea '{linea}': {str(e)}")
                            raise
                    
                    if not bloque:
                        break
                    
                    # Ordenar el bloque en memoria
                    bloque_ordenado = self.ordenar_bloque(bloque)
                    
                    # Crear y escribir archivo temporal
                    temp_file = self._create_temp_file('directa')
                    with open(temp_file, 'w') as temp:
                        for num in bloque_ordenado:
                            temp.write(f"{num:.1f}\n")
                    bloques_temp.append(temp_file)
            
            # Si no hay bloques que procesar, copiar entrada a salida
            if not bloques_temp:
                print("No se encontraron datos para ordenar")
                return
            
            # Mezclar todos los bloques ordenados
            self.merge_files(bloques_temp, ruta_salida)
            
        except Exception as e:
            print(f"Error durante la mezcla directa: {str(e)}")
            traceback.print_exc()
            raise
        finally:
            self.cleanup()

def crear_archivo_prueba(nombre_archivo, cantidad):
    """Crea un archivo con números aleatorios"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(script_dir, nombre_archivo)
    with open(ruta_completa, 'w') as f:
        for _ in range(cantidad):
            f.write(f"{random.uniform(1, 10000):.1f}\n")

def mostrar_numeros(archivo, n=10):
    """Muestra los primeros n números del archivo"""
    try:
        with open(archivo, 'r') as f:
            return [float(linea.strip()) for linea in f.readlines()[:n]]
    except Exception as e:
        print(f"Error al leer archivo {archivo}: {str(e)}")
        return []

if __name__ == "__main__":
    try:
        directorio = os.path.dirname(__file__)
        entrada = os.path.join(directorio, "numeros_desordenados.txt")
        salida = os.path.join(directorio, "numeros_ordenados.txt")
        
        print("Demostración de Ordenamiento Externo - Mezcla Directa")
        print("===================================================")
        
        # Crear archivo de prueba
        print("\nCreando archivo con números aleatorios...")
        crear_archivo_prueba(entrada, 1000)
        nums_originales = mostrar_numeros(entrada)
        print("Primeros números del archivo original:", nums_originales)
        
        if not nums_originales:
            print("Error: No se pudo leer el archivo de entrada")
            exit(1)
        
        # Ordenar usando bloques pequeños para demostración
        print("\nOrdenando archivo...")
        sorter = MezclaDirecta()
        sorter.mezcla_directa(entrada, salida, tamaño_bloque=100)
        
        nums_ordenados = mostrar_numeros(salida)
        if nums_ordenados:
            print("Primeros números del archivo ordenado:", nums_ordenados)
            
            # Verificar que esté ordenado
            ordenado = True
            anterior = float('-inf')
            
            with open(salida, 'r') as f:
                for linea in f:
                    try:
                        actual = float(linea.strip())
                        if actual < anterior:
                            ordenado = False
                            print(f"Error: Número {actual} está después de {anterior}")
                            break
                        anterior = actual
                    except ValueError as e:
                        print(f"Error al convertir línea '{linea.strip()}': {str(e)}")
                        ordenado = False
                        break
                    
            print("\nArchivo ordenado correctamente:", ordenado)
        else:
            print("Error: No se pudo leer el archivo de salida")
            
    except Exception as e:
        print(f"Error durante la ejecución: {str(e)}")
        traceback.print_exc()
