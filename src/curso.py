from estudiante import Estudiante


class Curso:
    def __init__(self, nombre_curso: str) -> None:
        self.nombre_curso: str = nombre_curso
        self.lista_estudiantes: list = []

    def add_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)