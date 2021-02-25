def print_file():
    with open("class.txt", mode="r", encoding="utf-8") as f:
        num = 0
        for line in f:
            print("Строка", num + 1)
            l = line.split(" ")
            print("Количество слов", len(l))
            print("Количество символов", len(line))
        print("Количество строк:", num)


print_file()
