import PySimpleGUI as Sb
import zipfile


def extract(archive_path, destination_path):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_path)


label_sel = Sb.Text("Select archive :")
in_sel = Sb.InputText()
choose_bt = Sb.FileBrowse('Choose File', key='archive')

label_fol = Sb.Text("Select folder :")
in_fol = Sb.InputText()
choose_bt2 = Sb.FolderBrowse('Choose Folder', key='folder')

archive_bt = Sb.Button('Extract', key='Extract')
output_label = Sb.Text(key="output", text_color="green")
window = Sb.Window('Extractor', layout=[[label_sel, in_sel, choose_bt],
                                        [label_fol, in_fol, choose_bt2],
                                        [archive_bt, output_label]])

while True:
    event, value = window.read()
    if event == "Extract":
        window['output'].update(value='Extracting.....')
        extract(value['archive'], value['folder'])
        window['output'].update(value='Files Extracted Successfully.')
    if event == Sb.WIN_CLOSED:
        break
window.close()
