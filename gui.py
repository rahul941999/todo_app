import functions
import PySimpleGUI as gui


label = gui.Text("Type a ToDo : ")
input_txt = gui.InputText(tooltip='Enter ToDo', key='todo')
add_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.read(), key='todos',
                       enable_events=True, size=[40, 12])
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
window = gui.Window(" ToDo App",
                    layout=[[label], [input_txt, add_button], [list_box, edit_button]])
while True:
    event, value = window.read()
    print(f"Event = {event} \nValue = {value}")
    match event:
        case "Add":
            todos = functions.read()
            todos.append(value['todo'] + '\n')
            functions.write(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_edit = value['todos'][0]
            new_todo = value['todo']
            todos = functions.read()
            index = todos.index(todo_edit)
            todos[index] = new_todo + '\n'
            functions.write(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case 'complete':
            todo_complete = value['todos'][0]
            todos = functions.read()
            index = todos.index(todo_complete)
            todos.pop(index)
        case gui.WIN_CLOSED:
            break
window.close()
