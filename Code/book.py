# Book.py
import storage

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
Manages the book operations in the library.
"""
class BookManager:
    
    """Initialize the BookManager with the given storage file.
    Args:
    - storage_file (str): The file path to store book data.
    """
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.books = storage.load_data(storage_file)

    """Save the current book data to the storage file."""
    def save_books(self):
        storage.save_data(self.storage_file, self.books)

    def is_isbn_unique(self, isbn):
        """
        Check if the given ISBN is unique in the library.
        Args:
        - isbn (str): The ISBN to check.
        Returns:
        - bool: True if the ISBN is unique, False otherwise.
        """
        for book in self.books:
            if book['isbn'] == isbn:
                return False
        return True

    def add_book(self, title, author, isbn):
        if not self.is_isbn_unique(isbn):
            print(f"ISBN {isbn} already exists. Cannot add duplicate books.")
            return
        book = Book(title, author, isbn)
        self.books.append(book.__dict__)
        self.save_books()

    """
    Update the information of a book in the library based on a specific attribute.

    Args:
    - search_key (str): The attribute to search on (e.g., 'title', 'author', 'isbn').
    - search_value: The value to search for in the specified attribute.
    - **kwargs: Any attributes of the book to update and their new values.
    """
    def update_book(self, isbn, **kwargs):
        for book in self.books:
            if book["isbn"] == isbn:
                for key, value in kwargs.items():
                    book[key] = value
                self.save_books()  # Save the changes to the file
                break


    """Delete a book from the library.
    Args:
    - isbn (str): The ISBN of the book to delete.
    """
    def delete_book(self, isbn):
        try:
            self.books = [book for book in self.books if book['isbn'] != isbn]
            self.save_books()
        except Exception as e:
            print(f"Error deleting book: {e}")

    """List all books in the library."""
    def list_books(self):
        try:
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Availability: {book.get('availability', True)}")
        except Exception as e:
            print(f"Error listing books: {e}")

    """Search for a book in the library based on a specific attribute. 
    Args:
    - key (str): The attribute to search on (e.g., 'title', 'author', 'isbn').
    - value: The value to search for in the specified attribute.
    """
    def search_book(self, key, value):
        try:
            found_books = []
            for book in self.books:
                if book.get(key) == value:
                    found_books.append(book)
            return found_books
        except Exception as e:
            print(f"Error searching book: {e}")
            return []
    
    def get_book(self, isbn):
        """
        Get the book with the given ISBN.
        Args:
        - isbn (str): The ISBN of the book to retrieve.
        Returns:
        - dict: The book information if found, None otherwise.
        """
        try:
            for book in self.books:
                if book['isbn'] == isbn:
                    return book
            return None
        except Exception as e:
            print(f"Error getting book: {e}")
            return None

        
        