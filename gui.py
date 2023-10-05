import functions
import PySimpleGUI as gui


label = gui.Text("Type a ToDo : ")
input_txt = gui.InputText(tooltip='Enter ToDo')
add_button = gui.Button('Add')
window = gui.Window(" ToDo App", layout=[[label],[input_txt,add_button]])
window.read()
window.close()