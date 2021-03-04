from tkinter import *
from tkinter import ttk
import os


class Tab1(Frame):
    def __init__(self, window):
        super(Tab1, self).__init__(window)
        self.lbl = Label(self, text="Путь")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(self, width=25)
        self.txt.grid(column=1, row=0)
        self.btn = Button(self, text="Выполнить", command=self.clicked)
        self.btn.grid(column=2, row=0)
        self.res = Text(self)
        self.res.config(state=DISABLED)
        self.res.grid(column=0, row=1, columnspan=5)

    def clicked(self):
        self.res.config(state=NORMAL)
        self.res.delete("1.0", END)
        self.res.config(state=DISABLED)
        self.print_path(self.txt.get())

    def print_path(self, path):
        res_str = ""
        for i in os.walk(path):
            for j in i[2]:
                path = i[0] + '/' + j
                res_str += path + "\n"
        self.res.config(state=NORMAL)
        self.res.insert("1.0", res_str)
        self.res.config(state=DISABLED)


class Tab2(Frame):
    def __init__(self, window):
        super(Tab2, self).__init__(window)
        self.lbl = Label(self, text="Разделитель")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(self, width=25)
        self.txt.grid(column=1, row=0)
        self.btn = Button(self, text="Выполнить", command=self.clicked)
        self.btn.grid(column=2, row=0)
        self.res = Label(self)
        self.res.grid(column=0, row=1, columnspan=3)

    def clicked(self):
        self.res.configure(text="")
        self.print_file(self.txt.get())

    def print_file(self, sep):
        with open("hello.txt", mode="r", encoding="utf-8") as f:
            lt = []
            data = f.read()
            l = data.split(sep)
            for s in l:
                lt.append(s)
            self.res.configure(text=lt)


class Tab3(Frame):
    def __init__(self, window):
        super(Tab3, self).__init__(window)
        self.lbl = Label(self, text="Текст")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(self, width=25)
        self.txt.grid(column=1, row=0)
        self.btn = Button(self, text="Выполнить", command=self.clicked)
        self.btn.grid(column=2, row=0)
        self.res = Label(self)
        self.res.grid(column=0, row=1, columnspan=3)

    def clicked(self):
        self.res.configure(text="")
        self.write_file(self.txt.get())

    def write_file(self, text):
        with open("hello2.txt", mode="a", encoding="utf-8") as f:
            f.write(text + "\n\n")
            self.res.configure(text="Файл записан")


class Tab4(Frame):
    def __init__(self, window):
        super(Tab4, self).__init__(window)
        self.btn = Button(self, text="Выполнить", command=self.clicked)
        self.btn.grid(column=0, row=0)
        self.res = Label(self)
        self.res.grid(column=0, row=1, columnspan=3)

    def clicked(self):
        self.res.configure(text="")
        self.print_file()

    def print_file(self):
        with open("class.txt", mode="r", encoding="utf-8") as f:
            num = 0
            summ = 0
            res_str = ""
            for line in f:
                l = line.split(" ")
                grade = int(l[2])
                num += 1
                summ += grade
                if grade < 3:
                    res_str += line + "\n"
            res_str += "Средний балл:" + str(summ // num)
            self.res.configure(text=res_str)


class Tab5(Frame):
    def __init__(self, window):
        super(Tab5, self).__init__(window)
        self.btn = Button(self, text="Выполнить", command=self.clicked)
        self.btn.grid(column=0, row=0)
        self.res = Text(self)
        self.res.config(state=DISABLED)
        self.res.grid(column=0, row=1, columnspan=3)

    def clicked(self):
        self.res.config(state=NORMAL)
        self.res.delete("1.0", END)
        self.res.config(state=DISABLED)
        self.print_file()

    def print_file(self):
        with open("class.txt", mode="r", encoding="utf-8") as f:
            num = 0
            res_str = ""
            for line in f:
                res_str += "Строка" + str(num + 1) + "\n"
                l = line.split(" ")
                res_str += "Количество слов: " + str(len(l)) + "\n"
                res_str += "Количество символов: " + str(len(line)) + "\n"
                num += 1
            res_str += "Количество строк: " + str(num)
            self.res.config(state=NORMAL)
            self.res.insert("1.0", res_str)
            self.res.config(state=DISABLED)


root = Tk()
root.geometry("485x510+200+200")
root.title("ПР10")
root.resizable(False, False)
tab_control = ttk.Notebook(root)
tab1 = Tab1(tab_control)
tab_control.add(tab1, text='Первая')
tab2 = Tab2(tab_control)
tab_control.add(tab2, text='Вторая')
tab3 = Tab3(tab_control)
tab_control.add(tab3, text='Третья')
tab4 = Tab4(tab_control)
tab_control.add(tab4, text='Четвертая')
tab5 = Tab5(tab_control)
tab_control.add(tab5, text='Пятая')
tab_control.pack(expand=1, fill='both')
root.mainloop()
