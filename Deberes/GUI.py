import Funciones
import FreeSimpleGUI as sg

label = sg.Text("Escribe un deber: ")
input = sg.InputText(tooltip="Ingresa un deber: ")
button = sg.Button("Agregar deber")

window = sg.Window('Mi App de Deberes', layout=[[label], [input, button]])
window.read()
window.close()

