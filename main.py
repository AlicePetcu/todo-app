import functions
import time

while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        with open('todos.txt', 'a') as file:
            file.write(todo)
    elif user_action.startswith('show'):
        todos_file = functions.get_todos()
        for i, item in enumerate(todos_file):
            show = f"{i + 1}.{item.strip('\n')}"
            print(show)
    elif user_action.startswith('edit'):
        try:
            index = int(user_action[5:])
            index = index - 1
            todos = functions.get_todos()
            new_todo = input("New todo: ")
            todos[index] = new_todo + '\n'
            functions.write_todos('todos.txt', todos)
        except ValueError:
            print('Your command is not valid')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            todos.pop(number - 1)
            functions.write_todos('todos.txt', todos)
        except IndexError:
            print('There is no item at this index')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print('Bye!')
