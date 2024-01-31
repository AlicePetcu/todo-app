import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter to-do", key='todo')
add_button = PySimpleGUI.Button('Add')
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=(45, 10))
edit_button = PySimpleGUI.Button('Edit')

window = PySimpleGUI.Window('To-do App',
                            layout=[[label], [input_box, add_button], [list_box, edit_button]],
                            font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo = values['todos'][0]
            new_todo = values['todo']

            todos_list = functions.get_todos()
            index = todos_list.index(todo)
            print(index)
            todos_list[index] = new_todo + '\n'
            functions.write_todos('todos.txt', todos_list)
            window['todos'].update(values=todos_list)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
