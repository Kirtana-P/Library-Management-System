# models.py

"""
Class Book represents a book in the library.
Attributes:
- title (str): The title of the book.
- author (str): The author of the book.
- isbn (str): The ISBN (International Standard Book Number) of the book.
- availability (bool): Indicates if the book is available for checkout.
"""
class Book:
    def __init__(self, title, author, isbn, availability=True, **kwargs):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

"""
Class User represents a user of the library.
Attributes:
- name (str): The name of the user.
- user_id (int): The unique identifier of the user.
"""
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

"""
Class Checkout represents a book checkout transaction.
Attributes:
- user_id (int): The user ID of the user checking out the book.
- isbn (str): The ISBN of the book being checked out.
- checkout_date (datetime): The date when the book was checked out.
"""
class Check:
    def __init__(self, user_id, isbn, checkout_date):
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = checkout_date