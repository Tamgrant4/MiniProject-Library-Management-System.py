#1. Class Structure 

class Book:
  def __init__(self, title, author, isbn, genre, publication_date, available=True):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.genre = genre
    self.publication_date = publication_date
    self.available = available

  def get_title(self):
    return self.title

  def set_title(self, new_title):
    self.title = new_title

  # Similar getter and setter methods for other attributes

  def __str__(self):
    return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nPublication Date: {self.publication_date}\nAvailable: {self.available}"

#3. User Interaction

import re

def get_int_input(message):
  while True:
    try:
      value = int(input(message))
      return value
    except ValueError:
      print("Invalid input. Please enter an integer.")

def get_string_input(message):
  return input(message)

def get_isbn_input():
  while True:
    isbn = get_string_input("Enter ISBN (13 digits): ")
    if re.match(r"^\d{13}$", isbn):
      return isbn
    else:
      print("Invalid ISBN format. Please enter 13 digits.")

#4. Main Menu

from book import Book
# Import other classes

def main_menu():
  print("\nWelcome to the Library Management System!")
  print("Main Menu:")
  print("1. Book Operations")
  print("2. User Operations")
  print("3. Author Operations")
  print("4. Genre Operations")
  print("5. Quit")

  choice = get_int_input("Enter your choice: ")
  return choice

def book_operations():
  # Implement functionalities like adding, borrowing, returning, searching books

def user_operations():
  # Implement functionalities like adding, viewing, displaying users

def author_operations():
  # Implement functionalities like adding, viewing, displaying authors

def genre_operations():
  # Implement functionalities like adding, viewing, displaying genres

if __name__ == "__main__":
  while True:
    choice = main_menu()
    if choice == 1:
      book_operations()
    elif choice == 2:
      user_operations()
    # Similar checks for other options
    elif choice == 5:
      print("Exiting the system...")
      break
    else:
      print("Invalid choice. Please try again.")
