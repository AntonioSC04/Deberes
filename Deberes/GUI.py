import Funciones
import FreeSimpleGUI as sg


label = sg.Text("Escribe un deber: ")
input = sg.InputText(tooltip="Ingresa un deber: ", key="deber")
button = sg.Button("Agregar")

window = sg.Window('Mi App de Deberes', layout=[[label], [input, button]],
                                             font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Agregar":
            deberes = Funciones.get_deberes()
            nuevo_deber = values['deber'] + "\n"
            deberes.append(nuevo_deber)
            Funciones.write_deberes(deberes)
        case sg.WIN_CLOSED:
            break

window.close()

