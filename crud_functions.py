import sqlite3

connection = sqlite3.connect('product_base.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
        );
    ''')


def get_all_products():
    products = cursor.execute('SELECT * FROM Products;').fetchall()
    connection.commit()
    return products


def add_user(username, email, age):
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES("{username}", "{email}", {age}, 1000);')
    connection.commit()


def is_included(username):
    user = cursor.execute(f'SELECT * FROM Users WHERE username = "{username}";').fetchone()
    connection.commit()
    if user is None:
        return False
    else:
        return True


# initiate_db()
# print(get_all_products())
# add_user('Murad', 'example@mail.ru', 48)
# if is_included('Noname'):
#     print('Ok')

connection.commit()
# connection.close()
