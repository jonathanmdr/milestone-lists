from utils.database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database.
"""


def start_database():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS book(name text primary key, author text, read integer)')


def add_book(name, author):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO book VALUES(?, ?, 0)', (name, author))


def get_all_books():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT name, author, read FROM book')
        books = [
            {
                'name': column[0],
                'author': column[1],
                'read': column[2]
            }
            for column in cursor.fetchall()
        ]

    return books


def mark_book_as_read(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE book SET read=1 WHERE name=?', (name,))


def delete_book(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM book WHERE name=?', (name,))
