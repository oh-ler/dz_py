def power(A, B):
    if B == 0:
        return 1
    else:
        return A * power(A, B - 1)

A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

result = power(A, B)

print(A, "в степени", B, "=", result)