def print_file():
    with open("class.txt", mode="r", encoding="utf-8") as f:
        num = 0
        summ = 0
        for line in f:
            l = line.split(" ")
            grade = int(l[2])
            num += 1
            summ += grade
            if grade < 3:
                print(line)
        print("Средний балл:", summ // num)


print_file()
