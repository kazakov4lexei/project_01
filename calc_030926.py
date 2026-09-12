# print ('q - закроет калькулятор')
# while True:
#     s = input('Введи знак +,-,*,/')
#     if s == 'q':
#         break
#     if s in ('+','-','*','/'):
#         x = float(input('Введи первое число'))
#         y = float(input('Введи второе число'))
#         if s == '+':
#             print (x + y)
#         elif s == '-':
#             print (x - y)
#         elif s == '*':
#             print (x * y)
#         elif s == '/':
#             if y != 0:
#                 print(x/y)
#             else:
#                 print('Делить на 0 нельзя')
#     else:
#         print('Введен не корректный знак операции')


print ('q - закроет калькулятор')
while True:
    s = input('Введи знак +,-,*,/,%')
    match s:
        case 'q':
            break
        case '+':
            x = float(input('Введи первое число'))
            y = float(input('Введи второе число'))
            print (x + y)
        case '-':
            x = float(input('Введи первое число'))
            y = float(input('Введи второе число'))
            print (x - y)
        case '*':
            x = float(input('Введи первое число'))
            y = float(input('Введи второе число'))
            print (x * y)
        case '/':
            x = float(input('Введи первое число'))
            y = float(input('Введи второе число'))
            if y != 0:
                print(x/y)
            else:
                print('Делить на 0 нельзя')
        case '%':
            print('Первое число - число от которого берем процент')
            print('Второе число - % который берем')
            x = float(input('Введи первое число'))
            y = float(input('Введи второе число'))
            print((x / 100) * y)
        case _:
            print('Введен не корректный знак операции')