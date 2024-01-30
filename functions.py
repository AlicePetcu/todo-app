def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_write):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_write)

