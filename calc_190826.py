# Калькулятор через elif

print("q - закроет программу")
while True:
    s = input("Введи знак: +,-,*,/   ")
    if s == "q":
        break
    if s in ("+","-","/","*"):
        x = float(input("Введи 1 число: "))
        y = float(input("Введи 2 число: "))
        if s == "+":
            print (x+y)
        elif s == "-":
            print (x-y)
        elif s == "*":
            print (x*y)
        elif s == "/":
            if y != 0:
                print (x/y)
            else:
                print ("Ты делишь на 0!!!")
    else:
        print ("Введен не корректный знак")


# Калькулятор через match case

# print('q - закроет программу')
# while True:
#     s = input('Введи знак: +,-,*,/   ')
#     match s:
#         case 'q':
#             break
#         case '+':
#             x = float(input('Введи 1 число: '))
#             y = float(input('Введи 2 число: '))
#             print (x+y)
#         case '-':
#             x = float(input('Введи 1 число: '))
#             y = float(input('Введи 2 число: '))
#             print (x-y)
#         case '*':
#             x = float(input('Введи 1 число: '))
#             y = float(input('Введи 2 число: '))
#             print (x*y)
#         case '/':
#             x = float(input('Введи 1 число: '))
#             y = float(input('Введи 2 число: '))
#             if y != 0:
#                 print (x/y)
#             else:
#                 print ('Ты делишь на 0!!!')
#         case _:
#             print ('Введен не корректный знак')

