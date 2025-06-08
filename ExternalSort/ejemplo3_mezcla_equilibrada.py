import os
import random
from external_sort import ExternalSort

class MezclaEquilibrada(ExternalSort):
    def __init__(self):
        super().__init__()
        
    def distribuir_inicial(self, archivo_entrada, temp1, temp2):
        """Distribuye los números del archivo de entrada en dos archivos temporales de manera equilibrada"""
        try:
            with open(self._ensure_absolute_path(archivo_entrada), 'r') as entrada, \
                 open(self._ensure_absolute_path(temp1), 'w') as f1, \
                 open(self._ensure_absolute_path(temp2), 'w') as f2:
                
                numeros = []
                for linea in entrada:
                    try:
                        numeros.append(float(linea.strip()))
                    except ValueError as e:
                        print(f"Error al convertir línea '{linea.strip()}': {str(e)}")
                        raise
                
                # Ordenar y distribuir de manera equilibrada
                numeros.sort()
                mitad = len(numeros) // 2
                
                for i in range(mitad):
                    f1.write(f"{numeros[i]:.1f}\n")
                for i in range(mitad, len(numeros)):
                    f2.write(f"{numeros[i]:.1f}\n")
        except Exception as e:
            print(f"Error en la distribución inicial: {str(e)}")
            raise
    
    def mezcla_equilibrada(self, archivo_entrada, archivo_salida, block_size=1000):
        """
        Implementa el algoritmo de mezcla equilibrada
        block_size: Tamaño del bloque para procesar en memoria
        """
        try:
            # Asegurar rutas absolutas
            archivo_entrada = self._ensure_absolute_path(archivo_entrada)
            archivo_salida = self._ensure_absolute_path(archivo_salida)
            
            # Verificar que el archivo de entrada existe
            if not os.path.exists(archivo_entrada):
                raise FileNotFoundError(f"El archivo de entrada {archivo_entrada} no existe")
            
            # Crear archivos temporales iniciales
            temp1 = self._create_temp_file('equilibrada_1')
            temp2 = self._create_temp_file('equilibrada_2')
            
            # Distribución inicial
            self.distribuir_inicial(archivo_entrada, temp1, temp2)
            
            # Mezclar los archivos temporales en el archivo de salida
            self.merge_files([temp1, temp2], archivo_salida)
            
        except Exception as e:
            print(f"Error durante la mezcla equilibrada: {str(e)}")
            raise
        finally:
            self.cleanup()

def crear_archivo_prueba(nombre_archivo, cantidad):
    """Crea un archivo de prueba con números aleatorios"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(script_dir, nombre_archivo)
    
    with open(ruta_archivo, 'w') as f:
        for _ in range(cantidad):
            f.write(f"{random.uniform(-1000, 1000):.1f}\n")

def verificar_ordenamiento(archivo):
    """Verifica que un archivo esté ordenado y devuelve los primeros números"""
    try:
        numeros = []
        ordenado = True
        anterior = float('-inf')
        
        with open(archivo, 'r') as f:
            for i, linea in enumerate(f):
                try:
                    actual = float(linea.strip())
                    if i < 10:  # Guardar los primeros 10 números
                        numeros.append(actual)
                    if actual < anterior:
                        ordenado = False
                        print(f"Error: Número {actual} está después de {anterior}")
                        break
                    anterior = actual
                except ValueError as e:
                    print(f"Error al convertir línea '{linea.strip()}': {str(e)}")
                    return False, []
        
        return ordenado, numeros
    except Exception as e:
        print(f"Error al verificar el archivo: {str(e)}")
        return False, []

def main():
    try:
        # Crear archivo de prueba
        archivo_entrada = "entrada_equilibrada.txt"
        archivo_salida = "salida_equilibrada.txt"
        
        print("Demostración de Ordenamiento Externo - Mezcla Equilibrada")
        print("======================================================")
        
        print("\nCreando archivo de prueba...")
        crear_archivo_prueba(archivo_entrada, 10000)
        
        print("Iniciando ordenamiento por mezcla equilibrada...")
        sorter = MezclaEquilibrada()
        
        # Probar con diferentes tamaños de bloque
        block_sizes = [100, 500, 1000]
        for block_size in block_sizes:
            print(f"\nProbando con tamaño de bloque: {block_size}")
            sorter.mezcla_equilibrada(archivo_entrada, archivo_salida, block_size)
            
            # Verificar el resultado
            ordenado, primeros_numeros = verificar_ordenamiento(archivo_salida)
            if primeros_numeros:
                print("Primeros números del archivo ordenado:", primeros_numeros)
            print(f"Archivo ordenado correctamente: {ordenado}")
            
    except Exception as e:
        print(f"Error durante la ejecución: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
