from tkinter import *


class Main(Frame):
    def __init__(self, window):
        super(Main, self).__init__(window)
        self.text = "0"
        self.field = Label(text=self.text, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.field.place(x=11, y=30)

        button_list = [
            "(", ")", "C", "DEL",
            "7", "8", "9", "/",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            ".", "0", "=", "*"
        ]

        x = 10
        y = 100

        for i in range(5):
            for j in range(4):
                bt = button_list[j + i * 4]
                button = Button(text=bt, bg="#000", fg="#FFF",
                                font=("Times New Roman", 15),
                                command=lambda c=bt: self.handle_op(c))
                button.place(x=x + j * 117, y=y + i * 81, width=115, height=79)

    def handle_op(self, operation):
        try:
            if operation == "C":
                self.text = ""
            elif operation == "DEL":
                self.text = self.text[0:-1]
            elif operation == "=":
                self.text = str(eval(self.text))
            else:
                if self.text == "0":
                    self.text = ""
                self.text += operation
            self.update_text()
        except ZeroDivisionError:
            self.field.configure(text="Ошибка")
            self.text = "0"
        except SyntaxError:
            self.field.configure(text="Ошибка")
            self.text = "0"

    def update_text(self):
        if self.text == "":
            self.text = "0"
        self.field.configure(text=self.text)


root = Tk()
root.configure(bg='#000')
root.geometry("485x510+200+200")
root.title("Калькулятор")
root.resizable(False, False)
app = Main(root)
app.pack()
root.mainloop()
