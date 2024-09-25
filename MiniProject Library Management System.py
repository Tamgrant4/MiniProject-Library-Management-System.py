class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_pub_date(self):
        return self.__pub_date

    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Pub Date: {self.__pub_date}, Borrowed: {self.__is_borrowed}"

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def borrow_book(self, book_title):
        if book_title not in self.__borrowed_books:
            self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def get_borrowed_books(self):
        return self.__borrowed_books

    def __str__(self):
        return f"User: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join(self.__borrowed_books)}"

class Author:
    def __init__(self, name, bio):
        self.__name = name
        self.__bio = bio

    def get_name(self):
        return self.__name

    def get_bio(self):
        return self.__bio

    def __str__(self):
        return f"Author: {self.__name}, Bio: {self.__bio}"

import re

def display_main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")
    return input("Select an option (1-4): ")

def display_book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    print("6. Back to Main Menu")
    return input("Select an option (1-6): ")

def display_user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    print("4. Back to Main Menu")
    return input("Select an option (1-4): ")

def display_author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    print("4. Back to Main Menu")
    return input("Select an option (1-4): ")

def validate_name(name):
    if re.match("^[A-Za-z ]+$", name):
        return True
    return False

def validate_id(library_id):
    if re.match("^[0-9]+$", library_id):
        return True
    return False

from book import Book
from user import User
from author import Author
import menu

books = []
users = []
authors = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    pub_date = input("Enter publication date: ")
    new_book = Book(title, author, genre, pub_date)
    books.append(new_book)
    print("Book added successfully.")

def borrow_book():
    title = input("Enter book title to borrow: ")
    for book in books:
        if book.get_title() == title:
            if book.borrow():
                print(f"You have borrowed {title}.")
            else:
                print(f"{title} is already borrowed.")
            return
    print("Book not found.")

def return_book():
    title = input("Enter book title to return: ")
    for book in books:
        if book.get_title() == title:
            if book.return_book():
                print(f"You have returned {title}.")
            else:
                print(f"{title} was not borrowed.")
            return
    print("Book not found.")

def display_books():
    if books:
        for book in books:
            print(book)
    else:
        print("No books available.")

def main():
    while True:
        choice = menu.display_main_menu()
        if choice == '1':  
            while True:
                book_choice = menu.display_book_menu()
                if book_choice == '1':
                    add_book()
                elif book_choice == '2':
                    borrow_book()
                elif book_choice == '3':
                    return_book()
                elif book_choice == '5':
                    display_books()
                elif book_choice == '6':
                    break
        elif choice == '4':
            print("Thank you for using the Library Management System!")
            break

if __name__ == "__main__":
    main()

from book import Book
from user import User
from author import Author
import menu

books = []
users = []
authors = []

# Book operations
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    pub_date = input("Enter publication date: ")
    new_book = Book(title, author, genre, pub_date)
    books.append(new_book)
    print("Book added successfully.")

def borrow_book():
    title = input("Enter book title to borrow: ")
    user_name = input("Enter your name: ")
    user_found = None

    for user in users:
        if user.get_name() == user_name:
            user_found = user
            break

    if not user_found:
        print("User not found.")
        return

    for book in books:
        if book.get_title() == title:
            if book.borrow():
                user_found.borrow_book(title)
                print(f"{user_name} has borrowed {title}.")
            else:
                print(f"{title} is already borrowed.")
            return
    print("Book not found.")

def return_book():
    title = input("Enter book title to return: ")
    user_name = input("Enter your name: ")
    user_found = None

    for user in users:
        if user.get_name() == user_name:
            user_found = user
            break

    if not user_found:
        print("User not found.")
        return

    for book in books:
        if book.get_title() == title:
            if book.return_book():
                user_found.return_book(title)
                print(f"{user_name} has returned {title}.")
            else:
                print(f"{title} was not borrowed.")
            return
    print("Book not found.")

def display_books():
    if books:
        for book in books:
            print(book)
    else:
        print("No books available.")

# User operations
def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    if menu.validate_name(name) and menu.validate_id(library_id):
        new_user = User(name, library_id)
        users.append(new_user)
        print("User added successfully.")
    else:
        print("Invalid name or library ID format.")

def view_user_details():
    library_id = input("Enter library ID to view details: ")
    for user in users:
        if user.get_library_id() == library_id:
            print(user)
            return
    print("User not found.")

def display_all_users():
    if users:
        for user in users:
            print(user)
    else:
        print("No users available.")

# Author operations
def add_author():
    name = input("Enter author name: ")
    bio = input("Enter author biography: ")
    if menu.validate_name(name):
        new_author = Author(name, bio)
        authors.append(new_author)
        print("Author added successfully.")
    else:
        print("Invalid author name format.")

def view_author_details():
    name = input("Enter author name to view details: ")
    for author in authors:
        if author.get_name() == name:
            print(author)
            return
    print("Author not found.")

def display_all_authors():
    if authors:
        for author in authors:
            print(author)
    else:
        print("No authors available.")

# Main program loop
def main():
    while True:
        choice = menu.display_main_menu()
        if choice == '1':  # Book Operations
            while True:
                book_choice = menu.display_book_menu()
                if book_choice == '1':
                    add_book()
                elif book_choice == '2':
                    borrow_book()
                elif book_choice == '3':
                    return_book()
                elif book_choice == '4':
                    title = input("Enter book title to search: ")
                    for book in books:
                        if book.get_title() == title:
                            print(book)
                            break
                    else:
                        print("Book not found.")
                elif book_choice == '5':
                    display_books()
                elif book_choice == '6':
                    break
        elif choice == '2':  # User Operations
            while True:
                user_choice = menu.display_user_menu()
                if user_choice == '1':
                    add_user()
                elif user_choice == '2':
                    view_user_details()
                elif user_choice == '3':
                    display_all_users()
                elif user_choice == '4':
                    break
        elif choice == '3':  # Author Operations
            while True:
                author_choice = menu.display_author_menu()
                if author_choice == '1':
                    add_author()
                elif author_choice == '2':
                    view_author_details()
                elif author_choice == '3':
                    display_all_authors()
                elif author_choice == '4':
                    break
        elif choice == '4':
            print("Thank you for using the Library Management System!")
            break

if __name__ == "__main__":
    main()
