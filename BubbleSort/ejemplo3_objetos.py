from bubble_sort import bubble_sort

class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
    
    def __str__(self):
        return f"{self.nombre} (Edad: {self.edad}, Promedio: {self.promedio})"
    
    def __lt__(self, other):
        return self.promedio < other.promedio

def ordenar_estudiantes(estudiantes):
    return bubble_sort(estudiantes)

# Ejemplo de ordenamiento de objetos
if __name__ == "__main__":
    # Crear lista de estudiantes
    estudiantes = [
        Estudiante("Juan", 20, 8.5),
        Estudiante("Ana", 19, 9.8),
        Estudiante("Pedro", 21, 7.6),
        Estudiante("María", 20, 9.1),
        Estudiante("Carlos", 22, 8.9)
    ]
    
    print("Lista original de estudiantes:")
    for estudiante in estudiantes:
        print(estudiante)
    
    # Ordenar por promedio
    estudiantes_ordenados = ordenar_estudiantes(estudiantes)
    
    print("\nLista de estudiantes ordenada por promedio:")
    for estudiante in estudiantes_ordenados:
        print(estudiante)
