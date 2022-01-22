

from database import get_books, book_list

welcome = "Welcome to the book database"

menu = '''
Select the correct option:
1) Add Book
2) View Book
3) Exit
'''

welcome = 'Welcome to the Book Database'
print(welcome)


def add_book():
    book_title = input("Name of the book?: ")
    book_author = input("Name of author?: ")

    book_list(book_title, book_author)


def view_books(entries):
    for entry in entries:
        print(f"{entry['title']}\n{entry['author']}\n")


while(selection := input(menu)) != '3':
    if(selection == '1'):
        add_book()
    elif(selection == '2'):
        view_books(get_books())
    else:
        print('Selection not allowed!')
