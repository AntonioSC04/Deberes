def get_deberes(filepath = "Deberes.txt"):
     with open(filepath, 'r') as file_local:
          deberes_local = file_local.readlines()
     return deberes_local


def write_deberes(deberes_arg, filepath = "Deberes.txt"):
     with open(filepath, 'w') as file:
          file.writelines(deberes_arg)

