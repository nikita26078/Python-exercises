def print_string(st):
    if len(st) > 10:
        st = st[:10]
    try:
        print(st[10])
    except IndexError:
        print("Обращение к индексу за пределами строки")
    finally:
        print("Ok")


s = input("Введите строку: ")
print_string(s)
