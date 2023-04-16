ticket_number = input("Введите номер билета: ")
sum_first_half = sum(map(int, ticket_number[:3]))
sum_second_half = sum(map(int, ticket_number[3:]))
if sum_first_half == sum_second_half:
    print("Билет счастливый!")
else:
    print("Билет несчастливый :(")