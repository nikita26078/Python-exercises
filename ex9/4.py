class BankAccount:

    def __init__(self, cl_id, first_name, last_name):
        self.client_id = cl_id
        self.client_first_name = first_name
        self.client_last_name = last_name
        self.balance = 0.0

    def add(self, val):
        self.balance += val

    def withdraw(self, val):
        if self.balance - val >= 0:
            self.balance -= val
        else:
            raise ValueError("Нельзя снять сумму больше, чем есть на балансе")


acc = BankAccount(0, "Ivan", "Ivanov")
try:
    acc.add(1000)
    acc.withdraw(5000)
except ValueError:
    print("Ошибка")
print(acc.balance)
