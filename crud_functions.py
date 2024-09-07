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


def get_all_products():
    products = cursor.execute('SELECT * FROM Products;').fetchall()
    connection.commit()
    return products


# initiate_db()
# print(get_all_products())


connection.commit()
# connection.close()
