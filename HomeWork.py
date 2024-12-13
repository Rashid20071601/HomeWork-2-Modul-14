# Import
import sqlite3


# Подключение к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


# Очистка таблицы перед заполнением
cursor.execute('DELETE FROM Users')


# Заполнение таблицы 10 записями
users = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000)
]


cursor.executemany('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', users)


# Обновление balance у каждой 2ой записи начиная с 1ой
cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = 1',
               (500,))


# Удаление каждой 3ей записи начиная с 1ой
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')


# Проверка изменений
cursor.execute('SELECT * FROM Users WHERE age != ?',
               (60,))
result = cursor.fetchall()

# Печать результата
for user in result:
    username, email, age, balance = user[1], user[2], user[3], user[4]
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')


# ==== ВАРИАНТ-1 ====
# Удаление пользователя с id=6
cursor.execute('DELETE FROM Users WHERE age = 60')

# Подсчёт кол-ва всех пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

'''
# ==== ВАРИАНТ-2 ====
cursor.execute('SELECT AVG(balance) FROM Users')
result = cursor.fetchone()[0]
print(result)
'''

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()