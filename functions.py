FILEPATH = "todos.txt"


def read(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
