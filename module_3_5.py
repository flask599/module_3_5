print('Рекурсивное умножение цифр')
print('-------------------------------')
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if str_number[-1] == '0':
       str_number = str_number[:-1]
# при выполнении задачи по пунктам данным в работе, без этого условия вывод на консоль
# получается:
    # 24
    # 0

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
result3 = get_multiplied_digits(4020301)
print(result3)
result4 = get_multiplied_digits(40203010)
print(result4)