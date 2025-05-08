import Funciones
import FreeSimpleGUI as sg
import time

sg.theme("DarkTeal11")

clock = sg.Text('', key='clock')
label = sg.Text("Escribe un deber: ")
input = sg.InputText(tooltip="Ingresa un deber: ", key="deber")
add_button = sg.Button(image_size=(60,36), image_source="Agregar.png", mouseover_colors="LightBlue2", tooltip="Ingresa un deber", key="Agregar")
list_box = sg.Listbox(values=Funciones.get_deberes(), key="deberes", enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Editar")
exit_button = sg.Button("Salir")

complete_button = sg.Button(image_size=(60,52), image_source="Completar.png", mouseover_colors="LightBlue2", tooltip="Completa tu deber", key="Completar")

window = sg.Window('Mi App de Deberes', layout=[[clock], [label],
                                                [input, add_button],
                                                [list_box, edit_button, complete_button],
                                                [exit_button]],
                                             font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%B %d, %Y %H:%M:%S"))


    match event:
        case "Agregar":
            deberes = Funciones.get_deberes()
            nuevo_deber = values['deber'].capitalize() + "\n"
            deberes.append(nuevo_deber)
            Funciones.write_deberes(deberes)
            window['deberes'].update(values=deberes)
            window['deber'].update(value='')

        case "Editar":
            try:
                deber_a_editar = values['deberes'][0]
                nuevo_deber = values['deber']

                deberes = Funciones.get_deberes()
                index = deberes.index(deber_a_editar)
                deberes[index] = nuevo_deber
                Funciones.write_deberes(deberes)
                window['deberes'].update(values=deberes)
            except IndexError:
                sg.popup('Selecciona un deber', font=('Helvetica', 10))

        case "Completar":
            try:
                deber_completado = values['deberes'][0]
                deberes = Funciones.get_deberes()
                deberes.remove(deber_completado)
                Funciones.write_deberes(deberes)
                window['deberes'].update(values=deberes)
                window['deber'].update(value='')
            except IndexError:
                sg.popup('Selecciona un deber', font=('Helvetica', 12))

        case "Salir":
            break

        case "deberes":
            window['deber'].update(value=values['deberes'][0])

        case sg.WIN_CLOSED:
            break

window.close()

