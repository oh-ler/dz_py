n = int(input("Введите количество элементов в массиве: "))
a = list(map(int, input("Введите элементы массива через пробел: ").split()))
x = int(input("Введите число X: "))

closest = min(a, key=lambda num: abs(num - x))

print("Ближайший элемент к числу X в массиве A:", closest)