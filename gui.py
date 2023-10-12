import functions
import PySimpleGUI as gui
import time

gui.theme("DarkBlack")

label_time = gui.Text("", key='clock')
label = gui.Text("Type a ToDo : ")
input_txt = gui.InputText(tooltip='Enter ToDo', key='todo')
add_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.read(), key='todos',
                       enable_events=True, size=[40, 12])
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
rc_content = [[edit_button], [complete_button]]
right_col = gui.Column(rc_content)
exit_button = gui.Button('Exit')
window = gui.Window(" ToDo App",
                    layout=[[label_time],
                            [label], [input_txt, add_button],
                            [list_box, right_col],
                            [exit_button]])
while True:
    event, value = window.read(timeout=500)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(f"Event = {event} \nValue = {value}")
    match event:
        case "Add":
            if value['todo'] != "":
                todos = functions.read()
                todos.append(value['todo'] + '\n')
                functions.write(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            else:
                gui.popup("Please Enter a todo to add", font=('Helvetica', 12))
        case 'Edit':
            try:
                todo_edit = value['todos'][0]
                new_todo = value['todo']
                todos = functions.read()
                index = todos.index(todo_edit)
                todos[index] = new_todo + '\n'
                functions.write(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                gui.popup("Please select an item first", font=('Helvetica', 12))
        case 'todos':
            window['todo'].update(value=value['todos'][0].strip("\n"))
        case 'Complete':
            try:
                todo_complete = value['todos'][0]
                todos = functions.read()
                index = todos.index(todo_complete)
                print(todos)
                todos.pop(index)
                print(todos)
                functions.write(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                gui.popup("Please select an item first", font=('Helvetica', 12))
        case 'Exit':
            window.close()
            exit()
        case gui.WIN_CLOSED:
            break
window.close()
