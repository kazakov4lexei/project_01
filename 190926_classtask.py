import sqlite3

# Задача 1 создание таблиц 
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# sql_querry = """CREATE TABLE IF NOT EXISTS Teacher ( 
# Teacher_Id INTEGER NOT NULL PRIMARY KEY, 
# Teacher_Name TEXT NOT NULL, 
# School_Id INTEGER NOT NULL, 
# Joining_Date TEXT NOT NULL, 
# Speciality TEXT NOT NULL, 
# Salary INTEGER NOT NULL,
# Experience INTEGER);"""
# cursor.execute(sql_querry)
# connection.commit()
# sql_querry_2 = """INSERT INTO Teacher (Teacher_Id, Teacher_Name, School_Id, 
# Joining_Date, Speciality, Salary, Experience) 
# VALUES 
# ('101', 'Галина', '1', '2021-2-10', 'Физик', '40000', NULL), 
# ('102', 'Мария', '1', '2018-07-23', 'Химик', '20000', NULL), 
# ('103', 'Ольга', '2', '2022-05-19', 'Информатик', '25000', NULL), 
# ('104', 'Полина', '2', '2017-12-28', 'Физик', '28000', NULL), 
# ('105', 'Лидия', '3', '2015-06-04', 'Информатик', '42000', NULL), 
# ('106', 'Анастасия', '3', '2019-09-11', 'Трудовик', '30000', NULL), 
# ('107', 'Ирина', '4', '2020-08-21', 'Информатик', '32000', NULL), 
# ('108', 'Виктория', '4', '2017-10-17', 'Географ', '30000', NULL);"""
# cursor.execute(sql_querry_2)
# connection.commit()
# connection.close()


# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM Teacher;')
# result = cursor.fetchall()
# connection.close()
# for i in result:
#     print(i)


def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_con(connection):
    if connection:
        connection.close()

# Задача 2
def read_db_version():
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute('SELECT sqlite_version();')
        version = cur.fetchone()
        close_con(con)
        print('Вы подключились к SQLite версии:', version[0])
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)

# Задача 3
def upd_exp():
    try:
        con = get_connection()
        cur = con.cursor()
        upd_querry = """UPDATE Teacher SET Experience = 20 WHERE School_Id = 4;"""
        cur.execute(upd_querry)
        con.commit()
        close_con(con)   
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)

# Задача 4

def get_school(school_id):
    try:
        con = get_connection()
        cur = con.cursor()
        query = """SELECT * FROM School WHERE School_Id = ?"""
        cur.execute(query,(school_id,))
        result = cur.fetchall()
        close_con(con)
        for row in result:
            print('ID школы:', row[0])
            print('Название школы:', row[1])
            print('Количество мест:', row[2])
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)

def get_teacher(teacher_id):
    try:
        con = get_connection()
        cur = con.cursor()
        query = """SELECT * FROM Teacher WHERE Teacher_Id = ?"""
        cur.execute(query,(teacher_id,))
        result = cur.fetchall()
        print(result)
        for row in result:
            print('ID Учителя:', row[0])
            print('Имя учителя:', row[1])
            print('ID школы:', row[2])
            print('Дата начала работы:', row[3])
            print('Специализация:', row[4])
            print('Зарплата:', row[5])
            print('Опыт работы:', row[6])   
        close_con(con)
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)

# Задача 5
        
def get_teacher_scpec(spec,sal):
    try:
        con = get_connection()
        cur = con.cursor()
        query = """SELECT * FROM Teacher WHERE speciality = ? and salary > ?"""
        cur.execute(query,(spec,sal))
        result = cur.fetchall()
        print(result)
        for row in result:
            print('ID Учителя:', row[0])
            print('Имя учителя:', row[1])
            print('ID школы:', row[2])
            print('Дата начала работы:', row[3])
            print('Специализация:', row[4])
            print('Зарплата:', row[5])
            print('Опыт работы:', row[6], '\n')   
        close_con(con)
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)

# Задача 6 Вариант 1 через ДЖОИН
        
def get_teacher_2(school_id):
    try:
        con = get_connection()
        cur = con.cursor()
        query = """SELECT * FROM Teacher JOIN School ON Teacher.School_Id = School.School_Id WHERE Teacher.School_Id = ?"""
        cur.execute(query,(school_id,))
        result = cur.fetchall()
        print(result)
        for row in result:
            print('ID Учителя:', row[0])
            print('Имя учителя:', row[1])
            print('ID школы:', row[2])
            print('Наименование школы: ', row[8])
            print('Дата начала работы:', row[3])
            print('Специализация:', row[4])
            print('Зарплата:', row[5])
            print('Опыт работы:', row[6], '\n')   
        close_con(con)
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)

# Задача 6 Вариант 2 через 2 функции
        
def get_teacher_3(school_id):
    try:
        con = get_connection()
        cur = con.cursor()
        query = """SELECT * FROM Teacher  WHERE School_Id = ?"""
        cur.execute(query,(school_id,))
        result = cur.fetchall()
        print(result)
        for row in result:
            print('ID Учителя:', row[0])
            print('Имя учителя:', row[1])
            print('ID школы:', row[2])
            print('Наименование школы: ', get_school_3(school_id))
            print('Дата начала работы:', row[3])
            print('Специализация:', row[4])
            print('Зарплата:', row[5])
            print('Опыт работы:', row[6], '\n')   
        close_con(con)
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)

def get_school_3(school_id):
    try:
        con = get_connection()
        cur = con.cursor()
        query = """SELECT * FROM School WHERE School_Id = ?"""
        cur.execute(query,(school_id,))
        result = cur.fetchone()
        close_con(con)
        return result[1]
    except (Exception, sqlite3.Error) as er:
        print('Ошибки в следующем: ', er)


# Вывод наименований таблиц
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()

# cursor.execute("""SELECT * FROM sqlite_master WHERE type = 'table'""")
# tables = cursor.fetchall()
# connection.close()

# for table in tables:
#     #print(table) # информация о таблицах
#      print(table[1]) #названия таблиц
connection = sqlite3.connect('teachers.db')
cursor = connection.execute('SELECT * FROM Teacher')
colnames = cursor.description
connection.close()
print(colnames)
# for row in colnames:
#     print(row[0])