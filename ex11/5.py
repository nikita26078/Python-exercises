from tkinter import *


class Main(Frame):
    def __init__(self, window):
        super(Main, self).__init__(window)
        root.bind('<Motion>', self.motion)
        self.lbl = Label(text="0", font=("Times New Roman", 21, "bold"), foreground="#000", width=25)
        self.lbl.place(x=11, y=30)

    def motion(self, event):
        if event.widget == self.lbl:
            x, y = event.x, event.y
            txt = "x: " + str(x) + "; y: " + str(y)
            self.lbl.config(text=txt)


root = Tk()
root.geometry("485x510+200+200")
root.title("Мышь")
root.resizable(False, False)
app = Main(root)
app.pack()
root.mainloop()
