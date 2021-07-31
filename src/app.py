from tkinter import Tk
from tkinter.filedialog import askopenfilename

from curso import Curso
from estudiante import Estudiante


def parser_students(chars: list):
    str_students = ''
    str_students_parsed = str_students.join(chars).strip()

    # Separa estudiantes por coma
    list_students = str_students_parsed.split(',')

    students = []

    for student in list_students:
        student_props = student.split(';')
        student_name = student_props[0].replace('<', '').replace('"',
                                                                 '').strip()
        student_note = student_props[1].replace('>', '').strip()

        students.append(Estudiante(student_name, student_note))

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

    parser_students(students_chars)

    chars.pop(0)
    char_pointer = chars[0]

    # Extraer Parametro
    param = ''
    param_parsed = param.join(chars).strip()


def load_file():
    Tk().withdraw()
    filename = askopenfilename()
    input_file = open(filename, 'r+')

    array_chars = []

    for line in input_file.readlines():
        for char in line.strip():
            array_chars.append(char)

    parser(array_chars)


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
            print('reporte')
        elif opt == '3':
            print('HTML')
        elif opt == '4':
            break
        else:
            continue
