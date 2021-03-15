def to_set(lt):
    st = set(lt)
    return st, len(st)


a = [1, 2, 124, 1, 2, 3]
b = "test text"
print(to_set(a))
print(to_set(b))
