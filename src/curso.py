from estudiante import Estudiante


class Curso:
    def __init__(self, nombre_curso: str) -> None:
        self.nombre_curso: str = nombre_curso
        self.lista_estudiantes: list = []
        self.list_options: list = []

    def add_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def define_opt(self, option: str):
        self.list_options.append(option)

    def sort_asc(self):
        return sorted(self.lista_estudiantes, key=lambda e: e.nota)

    def sort_desc(self):
        return sorted(self.lista_estudiantes,
                      key=lambda e: e.nota,
                      reverse=True)

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

    def quantity(self):
        return len(self.lista_estudiantes)

    def print_curso(self):
        print('---- ---- ---- ----')
        print('Curso: {}'.format(self.nombre_curso))
        print('Cantidad de estudiantes: {}'.format(len(
            self.lista_estudiantes)))

        for estudiante in self.lista_estudiantes:
            print('Nombre: {}, Nota: {}'.format(estudiante.nombre,
                                                estudiante.nota))

        print('---- ---- ---- ----')

        for option in self.list_options:
            if option == 'ASC':
                print('Orden Ascendente:')
                for estudiante in self.sort_asc():
                    print('Nombre: {}, Nota: {}'.format(
                        estudiante.nombre, estudiante.nota))
            elif option == 'DESC':
                print('Orden Descendente:')
                for estudiante in self.sort_desc():
                    print('Nombre: {}, Nota: {}'.format(
                        estudiante.nombre, estudiante.nota))
            elif option == 'AVG':
                print('Promedio: {}'.format(self.promedio()))
            elif option == 'MIN':
                print('Nota minima: {}'.format(self.get_min()))
            elif option == 'MAX':
                print('Nota maxima: {}'.format(self.get_max()))
            elif option == 'APR':
                print('Estudiantes aprobados: {}'.format(
                    self.calc_aprobados()))
            elif option == 'REP':
                print('Estudiantes reprobados: {}'.format(
                    self.calc_reprobados()))

        print('---- ---- ---- ----')
