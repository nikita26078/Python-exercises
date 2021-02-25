def write_file():
    text = input("Введите текст: ")
    with open("hello2.txt", mode="a", encoding="utf-8") as f:
        f.write(text + "\n\n")


write_file()
