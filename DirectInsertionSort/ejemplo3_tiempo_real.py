from insertion_sort import insertion_sort
import time
import random

class ListaEnTiempoReal:
    def __init__(self):
        self.elementos = []
    
    def agregar_elemento(self, elemento):
        """Agrega un elemento y mantiene la lista ordenada"""
        self.elementos.append(elemento)
        return insertion_sort(self.elementos)
    
    def obtener_lista(self):
        return self.elementos

def simular_llegada_datos():
    """Simula la llegada de datos en tiempo real"""
    lista_tiempo_real = ListaEnTiempoReal()
    
    print("Simulando llegada de datos en tiempo real...")
    print("-------------------------------------------")
    
    # Simular 10 llegadas de datos
    for i in range(10):
        # Generar número aleatorio
        nuevo_elemento = random.randint(1, 100)
        
        print(f"\nLlegó nuevo elemento: {nuevo_elemento}")
        lista_ordenada = lista_tiempo_real.agregar_elemento(nuevo_elemento)
        print(f"Lista actual ordenada: {lista_ordenada}")
        
        # Pequeña pausa para simular tiempo real
        time.sleep(1)

# Ejemplo de ordenamiento en tiempo real
if __name__ == "__main__":
    print("Demostración de ordenamiento en tiempo real")
    print("==========================================")
    
    # Ejecutar simulación
    simular_llegada_datos()
    
    print("\nSimulación completada!")
