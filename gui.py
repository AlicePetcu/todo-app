import functions
import PySimpleGUI
import time

PySimpleGUI.theme('DarkBlack')

clock = PySimpleGUI.Text('', key='clock')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter to-do", key='todo')
add_button = PySimpleGUI.Button('Add')
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=(30, 5))
edit_button = PySimpleGUI.Button('Edit')
complete_button = PySimpleGUI.Button('Complete')

exit_button = PySimpleGUI.Button('Exit')

window = PySimpleGUI.Window('To-do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Baskerville', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.get_todos()
            if values['todo'][-1] == '\n':
                new_todo = values['todo']
            else:
                new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo = values['todos'][0]
                new_todo = values['todo']

                todos_list = functions.get_todos()
                index = todos_list.index(todo)
                print(index)
                todos_list[index] = new_todo + '\n'
                functions.write_todos('todos.txt', todos_list)
                window['todos'].update(values=todos_list)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup('Please select an item first', title='ERROR', font=('Baskerville', 15))
        case 'Complete':
            try:
                todo = values['todos'][0]
                todos_list = functions.get_todos()
                todos_list.remove(todo)
                functions.write_todos('todos.txt', todos_list)
                window['todos'].update(values=todos_list)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup('Please select an item first', font=('Baskerville', 15))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
