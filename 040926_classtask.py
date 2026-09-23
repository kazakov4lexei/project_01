
# print('Hello world!')

# a = 10

# def hello_func():
#     '''Функция делает...'''
#     for i in range(5):
#         print('Привет', i)


# print(hello_func.__doc__)

# def make_coffee(size, sugar_dose=3):
#     if sugar_dose > 5:
#         return 'Слишком много сахара! :('
#     else:
#         return f'Ваш кофе объемом {size} мл с {sugar_dose} кусочками сахара'

# print(make_coffee(5,500))


# my_list = [4, 7, 2, 5, 4]
# my_list = [[4, 7, 2, 5, 4], [7, 14, 1, 8, 3], [5, 1, 8, 2, 7]]

# def average(numbers):
#     print(f'Функцию вызвали с параметром {numbers}')
#     value = sum(numbers) / len(numbers)
#     return value

# for i in my_list:
#  print(average(i))


# Функция для добавления суперпользователя
# def add_root():
#     name = 'root'
#     uid = 0
#     return name, uid


# def tekst(x,y):
#     print('print inside tekst', x,y)


# def testfunc():
#     user_name, user_uid = add_root()
#     tekst(user_name,user_uid)

# testfunc()

# def testsum(x):
#     return x + x + x

# anon_func = lambda x: x + x + x
# print(testsum(3))
# print(anon_func(4))

# def trapezoid_s(a, b, h):
#     '''Функция для расчета площади 
#     трапеции. a - нижнее основание, b 
#     - верхнее основание, h - высота.'''
#     print(a,b,h)

#     return h * (a+b) / 2
# param_dict = {'a': 3, 'b': 7, 'h': 9}
# param_lst = (8, 4, 10, 5)

# S = trapezoid_s(*param_lst)

# print(S)
#dfdfdfdvfgf
def print_them_all(*args, **kwargs):
    print('print_them_all')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)

    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)

print_them_all(1,2,4,'fffkfkf',[1,32,45,True], True, a = 123, b = 'NDKGK', C = True)