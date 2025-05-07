import Funciones
import FreeSimpleGUI as sg


label = sg.Text("Escribe un deber: ")
input = sg.InputText(tooltip="Ingresa un deber: ", key="deber")
add_button = sg.Button("Agregar")
list_box = sg.Listbox(values=Funciones.get_deberes(), key="deberes", enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Editar")
exit_button = sg.Button("Salir")

complete_button = sg.Button("Completar")

window = sg.Window('Mi App de Deberes', layout=[[label],
                                                [input, add_button],
                                                [list_box, edit_button, complete_button],
                                                [exit_button]],
                                             font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["deberes"])

    match event:
        case "Agregar":
            deberes = Funciones.get_deberes()
            nuevo_deber = values['deber'].capitalize() + "\n"
            deberes.append(nuevo_deber)
            Funciones.write_deberes(deberes)
            window['deberes'].update(values=deberes)
            window['deber'].update(value='')

        case "Editar":
            deber_a_editar = values['deberes'][0]
            nuevo_deber = values['deber']

            deberes = Funciones.get_deberes()
            index = deberes.index(deber_a_editar)
            deberes[index] = nuevo_deber
            Funciones.write_deberes(deberes)
            window['deberes'].update(values=deberes)

        case "Completar":
            deber_completado = values['deberes'][0]
            deberes = Funciones.get_deberes()
            deberes.remove(deber_completado)
            Funciones.write_deberes(deberes)
            window['deberes'].update(values=deberes)
            window['deber'].update(value='')

        case "Salir":
            break

        case "deberes":
            window['deber'].update(value=values['deberes'][0])

        case sg.WIN_CLOSED:
            break

window.close()

