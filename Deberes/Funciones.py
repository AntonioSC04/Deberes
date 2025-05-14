import os

def get_deberes():
    carpeta_actual = os.path.dirname(__file__)
    filepath = os.path.join(carpeta_actual, "Deberes.txt")

    with open(filepath, 'r') as file_local:
        return file_local.readlines()

def write_deberes(deberes_arg):
    carpeta_actual = os.path.dirname(__file__)
    filepath = os.path.join(carpeta_actual, "Deberes.txt")

    with open(filepath, 'w') as file:
        file.writelines(deberes_arg)

