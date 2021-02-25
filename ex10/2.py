def print_file():
    sep = input("Введите разделитель: ")
    with open("hello.txt", mode="r", encoding="utf-8") as f:
        lt = []
        data = f.read()
        l = data.split(sep)
        for s in l:
            lt.append(s)
        print(lt)


print_file()
