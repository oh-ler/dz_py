n = int(input("Введите количество элементов в массиве: "))
a = list(map(int, input("Введите элементы массива через пробел: ").split()))
x = int(input("Введите число X: "))

count = a.count(x)

print("Число X встречается в массиве A", count, "раз(а).")