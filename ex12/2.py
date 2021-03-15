def diff(a, b, c, symmetric):
    if symmetric:
        return a ^ b ^ c
    else:
        return a - b - c


t1 = set("qwerty")
t2 = set("test")
t3 = set("text")
r = diff(t1, t2, t3, True)
print(r)
