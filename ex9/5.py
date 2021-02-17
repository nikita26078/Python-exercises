class NegativeValueException(Exception):
    def __init__(self, num):
        self.text = "Введено отрицательное число " + str(num)


def get_number():
    n = int(input("Введите число >= 0: "))
    if n < 0:
        raise NegativeValueException(n)
    print(n)


try:
    get_number()
except NegativeValueException as e:
    print(e.text)
