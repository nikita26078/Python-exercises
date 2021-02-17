class Notepad:

    def __init__(self):
        self.notes = []

    def add(self, note):
        self.notes.append(note)


notepad = Notepad()
try:
    notepad.remove(1)
except AttributeError:
    print("Нет такой функции в классе")
finally:
    print("Ok")
