import os


def print_path():
    path = input("Введите путь: ")
    for i in os.walk(path):
        for j in i[2]:
            path = i[0] + '/' + j
            print(path)


print_path()
