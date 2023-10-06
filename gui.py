import functions
import PySimpleGUI as gui


label = gui.Text("Type a ToDo : ")
input_txt = gui.InputText(tooltip='Enter ToDo', key='todo')
add_button = gui.Button('Add')
window = gui.Window(" ToDo App",
                    layout=[[label], [input_txt, add_button]])
while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = functions.read()
            todos.append(value['todo'] + '\n')
            functions.write(todos)
        case gui.WIN_CLOSED:
            break
window.close()
