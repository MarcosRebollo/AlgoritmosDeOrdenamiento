from binary_insertion_sort import binary_search, binary_insertion_sort
from dataclasses import dataclass
from typing import List

@dataclass
class Estudiante:
    id: int
    nombre: str
    promedio: float
    
    def __lt__(self, other):
        return self.promedio < other.promedio

def ordenar_estudiantes(estudiantes: List[Estudiante]) -> List[Estudiante]:
    """
    Ordena una lista de estudiantes por promedio usando binary insertion sort
    """
    return binary_insertion_sort(estudiantes)

if __name__ == "__main__":
    # Crear lista de estudiantes
    estudiantes = [
        Estudiante(1, "Ana", 9.5),
        Estudiante(2, "Carlos", 8.7),
        Estudiante(3, "Beatriz", 9.8),
        Estudiante(4, "David", 7.9),
        Estudiante(5, "Elena", 8.9),
        Estudiante(6, "Francisco", 9.2),
        Estudiante(7, "Gloria", 8.5)
    ]
    
    print("Lista original de estudiantes:")
    for e in estudiantes:
        print(f"ID: {e.id}, Nombre: {e.nombre}, Promedio: {e.promedio}")
    
    # Ordenar estudiantes por promedio
    estudiantes_ordenados = ordenar_estudiantes(estudiantes.copy())
    
    print("\nEstudiantes ordenados por promedio:")
    for e in estudiantes_ordenados:
        print(f"ID: {e.id}, Nombre: {e.nombre}, Promedio: {e.promedio}")
    
    # Demostrar búsqueda binaria
    print("\nDemostración de búsqueda binaria:")
    promedios = [e.promedio for e in estudiantes_ordenados]
    promedio_buscar = 8.8
    pos = binary_search(promedios, promedio_buscar, 0, len(promedios) - 1)
    print(f"Posición para insertar promedio {promedio_buscar}: {pos}")
    
    # Agregar nuevo estudiante
    nuevo = Estudiante(8, "Hugo", promedio_buscar)
    estudiantes_ordenados.insert(pos, nuevo)
    
    print("\nLista actualizada con nuevo estudiante:")
    for e in estudiantes_ordenados:
        print(f"ID: {e.id}, Nombre: {e.nombre}, Promedio: {e.promedio}")
