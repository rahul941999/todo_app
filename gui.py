import functions
import PySimpleGUI as Gui
import time
import os


Gui.theme("DarkBlack")

if not os.path.exists("todos.txt"):
    with open('todos.txt', "w") as file:
        pass

label_time = Gui.Text("", key='clock')
label = Gui.Text("Type a ToDo : ")
input_txt = Gui.InputText(tooltip='Enter ToDo', key='todo')
add_button = Gui.Button('Add', size=8)
list_box = Gui.Listbox(values=functions.read(), key='todos',
                       enable_events=True, size=(40, 12))
edit_button = Gui.Button('Edit', size=(7, 1))
complete_button = Gui.Button("Complete", key='Complete', size=(7, 1),
                             tooltip="Complete", mouseover_colors='LightBlue2')
rc_content = [[edit_button], [complete_button]]
right_col = Gui.Column(rc_content)
exit_button = Gui.Button('Exit', key="Exit", size=20)
window = Gui.Window(" ToDo App",
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
                Gui.popup("Please Enter a todo to add", font=('Helvetica', 12))
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
                Gui.popup("Please select an item first", font=('Helvetica', 12))
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
                Gui.popup("Please select an item first", font=('Helvetica', 12))
        case 'Exit':
            break
        case Gui.WIN_CLOSED:
            break
window.close()
