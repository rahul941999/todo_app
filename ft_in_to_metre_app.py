import PySimpleGUI as sg


def ft_to_mt(feet, inches):
    metre = feet * 0.3048 + inches * 0.0254
    print(f'metre = {metre}')
    return str(metre)


feet_label = sg.Text('Enter feet :')
feet_input = sg.InputText(key='feet')
inch_label = sg.Text('Enter Inches :')
inch_input = sg.InputText(key='inches')
convert_bt = sg.Button("Convert")
output_label = sg.Text("", key='output',text_color='white')
window = sg.Window("feet and inches to Metre", layout=[[feet_label, feet_input],
                                                       [inch_label, inch_input],
                                                       [convert_bt, output_label]])
while True:
    event, value = window.read()
    if event == 'Convert':
        print(f"Event = {event} \nValue = {value}")
        try:
            ft = float(value['feet'])
        except ValueError:
            ft = 0.0
        try:
            inc = float(value['inches'])
        except ValueError:
            inc = 0.0
        window['output'].update(value=ft_to_mt(ft, inc) + ' meters')
    if event == sg.WIN_CLOSED:
        print('Exiting !')
        break
window.close()

