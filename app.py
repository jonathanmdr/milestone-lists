from utils import database

USE_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()

    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    database.delete_book(name)


options = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book
}


def menu():
    database.start_database()

    user_input = input(USE_CHOICE)

    while user_input != 'q':
        if user_input in options:
            execution = options[user_input]
            execution()
        else:
            print('Unknown command. Please try again.')

        user_input = input(USE_CHOICE)


menu()
