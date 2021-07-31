from tkinter import Tk
from tkinter.filedialog import askopenfilename


def parser(chars: list):
    print(chars)
    print('Longitud: {}'.format(len(chars)))
    # Extraer nombre del curso
    course_name_chars = []
    char_pointer = chars[0]

    while char_pointer != '=':
        course_name_chars.append(chars.pop(0))
        char_pointer = chars[0]

    print(chars)
    print('Longitud: {}'.format(len(chars)))

    course_name = ''
    course_name_parsed = course_name.join(course_name_chars).strip()
    print('*{}*'.format(course_name_parsed))


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
