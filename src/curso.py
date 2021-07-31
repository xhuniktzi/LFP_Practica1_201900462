from estudiante import Estudiante


class Curso:
    def __init__(self, nombre_curso: str) -> None:
        self.nombre_curso: str = nombre_curso
        self.lista_estudiantes: list = []
        self.option: str = None

    def add_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def define_opt(self, option: str):
        self.option = option

        if option == 'ASC':
            self.sort_asc()
        if option == 'DESC':
            self.sort_desc()

    def sort_asc(self):
        self.lista_estudiantes.sort(key=lambda e: e.nota)

    def sort_desc(self):
        self.lista_estudiantes.sort(reverse=True, key=lambda e: e.nota)

    def promedio(self):
        suma = 0
        for estudiante in self.lista_estudiantes:
            suma += estudiante.nota

        return suma / len(self.lista_estudiantes)

    def get_min(self):
        return min(list(map(lambda e: e.nota, self.lista_estudiantes)))

    def get_max(self):
        return max(list(map(lambda e: e.nota, self.lista_estudiantes)))

    def calc_aprobados(self):
        count = 0
        for estudiante in self.lista_estudiantes:
            if estudiante.nota >= 61:
                count += 1

        return count

    def calc_reprobados(self):
        count = 0
        for estudiante in self.lista_estudiantes:
            if estudiante.nota < 61:
                count += 1

        return count

    def print_curso(self):
        print('---- ---- ---- ----')
        print('Curso: {}'.format(self.nombre_curso))
        print('Cantidad de estudiantes: {}'.format(len(
            self.lista_estudiantes)))

        for estudiante in self.lista_estudiantes:
            print('Nombre: {}, Nota: {}'.format(estudiante.nombre,
                                                estudiante.nota))

        if self.option == 'AVG':
            print('Promedio: {}'.format(self.promedio()))
        elif self.option == 'MIN':
            print('Nota minima: {}'.format(self.get_min()))
        elif self.option == 'MAX':
            print('Nota maxima: {}'.format(self.get_max()))
        elif self.option == 'APR':
            print('Estudiantes aprobados: {}'.format(self.calc_aprobados()))
        elif self.option == 'REP':
            print('Estudiantes reprobados: {}'.format(self.calc_reprobados()))

        print('---- ---- ---- ----')
