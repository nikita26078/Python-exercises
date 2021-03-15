def superset(a, b):
    if a > b:
        print(f'Объект {a} является чистым супермножеством')
    elif a < b:
        print(f'Объект {b} является чистым супермножеством')
    elif a == b:
        print('Множества равны')
    else:
        print('Супермножество не обнаружено')


set1 = {2, 9, 8, 5}
set2 = {8, 5}
set3 = {5, 8, 9, 2}
set4 = {32, 42, 55}

superset(set1, set2)
superset(set1, set3)
superset(set3, set2)
superset(set4, set2)
