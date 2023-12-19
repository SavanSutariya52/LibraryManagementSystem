class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added to the library.')

    def display_books(self):
        if not self.books:
            print('No books in the library.')
        else:
            print('Library Books:')
            for book in self.books:
                status = 'Available' if book.available else 'Borrowed'
                print(f'"{book.title}" by {book.author} - {status}')

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f'You have borrowed "{title}".')
                return
        print(f'Sorry, "{title}" is not available for borrowing.')

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f'Thank you for returning "{title}".')
                return
        print(f'Error: "{title}" was not borrowed from this library.')

def main():
    library = Library()

    while True:
        print('\nLibrary Management System')
        print('1. Add Book')
        print('2. Display Books')
        print('3. Borrow Book')
        print('4. Return Book')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            title = input('Enter the title of the book: ')
            author = input('Enter the author of the book: ')
            library.add_book(title, author)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input('Enter the title of the book you want to borrow: ')
            library.borrow_book(title)
        elif choice == '4':
            title = input('Enter the title of the book you want to return: ')
            library.return_book(title)
        elif choice == '5':
            print('Exiting the Library Management System. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()