from tkinter import Tk
from tkinter.filedialog import askopenfilename

from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader

from curso import Curso
from estudiante import Estudiante

from os import startfile

list_courses = []


def parser_students(chars: list):
    str_students = ''
    str_students_parsed = str_students.join(chars).strip()

    # Separa estudiantes por coma
    list_students = str_students_parsed.split(',')

    students = []

    for student in list_students:
        student_props = student.split(';')
        nombre = student_props[0].replace('<', '').replace('"', '').strip()
        nota = student_props[1].replace('>', '').strip()

        students.append(Estudiante(nombre, nota))

    return students


def parser(chars: list):
    # Extraer nombre del curso
    course_name_chars = []
    char_pointer = chars[0]

    while char_pointer != '=':
        course_name_chars.append(chars.pop(0))
        char_pointer = chars[0]

    course_name = ''
    course_name_parsed = course_name.join(course_name_chars).strip()

    # Crear objeto curso
    course = Curso(course_name_parsed)
    list_courses.append(course)

    # Encontrar llave de apertura
    while char_pointer != '{':
        chars.pop(0)
        char_pointer = chars[0]

    chars.pop(0)
    char_pointer = chars[0]

    # Explorar hasta encontrar cierre
    students_chars = []
    while char_pointer != '}':
        students_chars.append(chars.pop(0))
        char_pointer = chars[0]

    for student in parser_students(students_chars):
        course.add_estudiante(student)

    chars.pop(0)
    char_pointer = chars[0]

    # Extraer Parametro
    param = ''
    param_parsed = param.join(chars).strip()

    list_params = param_parsed.split(',')

    for param in list_params:
        course.define_opt(param.strip())


def load_file():
    try:
        Tk().withdraw()
        filename = askopenfilename()
        input_file = open(filename, 'r+', encoding='utf-8')
    except:
        print('Error al cargar el archivo')
    else:
        array_chars = []

        for line in input_file.readlines():
            for char in line.strip():
                array_chars.append(char)

        parser(array_chars)


def print_courses():
    for course in list_courses:
        course.print_curso()


def export_report():
    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))
    template = env.get_template('reports.html')

    html_file = open('index.html', 'w+', encoding='utf-8')
    html_file.write(template.render(list_courses=list_courses))
    html_file.close()

    startfile('index.html')


if __name__ == '__main__':
    while True:
        print('''
---- Menú ----
1. Cargar Archivo
2. Mostrar Reporte en Consola
3. Exportar Reporte
4. Salir
---- ---- ----
        ''')

        opt = input('Ingresa una opción: ')
        if opt == '1':
            load_file()
        elif opt == '2':
            print_courses()
        elif opt == '3':
            export_report()
        elif opt == '4':
            break
        else:
            continue