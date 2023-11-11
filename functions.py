FILEpath = 'todos.txt'

def get_todos(filepath=FILEpath):
    with open(filepath, 'r') as file_local:
        list1_local = file_local.readlines()
    return list1_local

def write_todos(todos_arg, filepath=FILEpath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print("Hello from functions")