import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter to-do", key='todo')
add_button = PySimpleGUI.Button('Add')

window = PySimpleGUI.Window('To-do App', layout=[[label], [input_box], [add_button]], font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos('todos.txt', todos)
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
