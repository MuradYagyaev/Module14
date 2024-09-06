import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Создание индекса (так, на всякий случай, может в будущем будем с этой базой работать)
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# Заполнение таблицы Users
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f"User{i}", f"example{i}@gmail.com", 10 * i, 1000))

# Обновление balance у каждой 2ой записи начиная с 1ой на 500:
# n = 1
# for i in range(1, 11):
#     if n == 1:
#         cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f"User{i}"))
#         n = 0
#     else:
#         n += 1

# Удаление каждой 3ей записи в таблице начиная с 1ой:
# n = 2
# for i in range(1, 11):
#     if n == 2:
#         cursor.execute('DELETE FROM Users WHERE username = ?', (f"User{i}",))
#         n = 0
#     else:
#         n += 1

# Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# Удаление из базы записи с id = 6
# cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))

# Подсчет общего количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f'Количество пользователей: {total_users}')

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(f'Общий баланс: {all_balances}')

# Средний баланс всех пользователей
cursor.execute('SELECT AVG(balance) FROM Users')
print(f'Средний баланс пользователеЙ: {cursor.fetchone()[0]}')
# Проверка SQL-функции
print(f'Средний баланс, полученный делением: {all_balances / total_users}')

connection.commit()
connection.close()
