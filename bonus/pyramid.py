n = int(input("Введите высоту пирамиды: "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i * 2 + 1))
