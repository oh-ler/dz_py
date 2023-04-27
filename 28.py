def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a - 1, b + 1)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

result = sum(A, B)

print("Сумма чисел", A, "и", B, "=", result)