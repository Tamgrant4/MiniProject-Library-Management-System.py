class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__available = True
    
    # Encapsulated attributes with getter and setter methods
    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__available

    def borrow_book(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def display_details(self):
        status = 'Available' if self.__available else 'Borrowed'
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Status: {status}"

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def borrow_book(self, book):
        if book.is_available():
            book.borrow_book()
            self.__borrowed_books.append(book.get_title())
            return True
        return False

    def return_book(self, book):
        if book.get_title() in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book.get_title())
            return True
        return False

    def display_user_details(self):
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join(self.__borrowed_books) if self.__borrowed_books else 'None'}"

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def display_author_details(self):
        return f"Author: {self.__name}, Biography: {self.__biography}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
    
    def display_main_menu(self):
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        return input("Select an option: ")
    
    def book_operations(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        return input("Select an option: ")

from library import Library # type: ignore

def main():
    library = Library()
    
    while True:
        choice = library.display_main_menu()
        
        if choice == '1':
            library.book_operations()
        elif choice == '2':
            library.user_operations()
        elif choice == '3':
            library.author_operations()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

def handle_invalid_input():
    print("Invalid input! Please enter a valid option.")

