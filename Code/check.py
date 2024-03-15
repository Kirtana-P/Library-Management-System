import json
from datetime import datetime
from book import BookManager

class CheckManager:
    def __init__(self, filename):
        """Initialize the CheckManager.
        Args:
        - filename (str): The path to the file storing checkouts data.
        - book_manager (BookManager): The BookManager instance for updating book availability.
        """
        self.filename = filename
        self.checkouts = []
        self.checkins = []
        self.load_checkouts()
        self.load_checkins()

    def save_checkouts(self):
        """Save the checkouts data to a file."""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.checkouts, file, indent=4)
        except Exception as e:
            print(f"Error saving checkouts data: {e}")
    
    def save_checkins(self):
        """Save the checkins data to a file."""
        try:
            with open("data/checkins.json", "w") as file:
                json.dump(self.checkins, file, indent=4)
        except Exception as e:
            print(f"Error saving checkins data: {e}")

    def load_checkouts(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()
                if data:
                    self.checkouts.extend(json.loads(data))  
                else:
                    self.checkouts = []
        except FileNotFoundError:
            self.checkouts = []
        except Exception as e:
            print(f"Error loading checkouts data: {e}")
            self.checkouts = []

    def load_checkins(self):
        try:
            with open("data/checkins.json", "r") as file:
                data = file.read()
                if data:
                    self.checkins = json.loads(data) 
                else:
                    self.checkins = []
        except FileNotFoundError:
            self.checkins = []
        except Exception as e:
            print(f"Error loading checkins data: {e}")
            self.checkins = []


    def list_checkouts(self):
        """List all checkouts."""
        try:
            if not self.checkouts:
                print("No checkouts found.")
            else:
                for checkout in self.checkouts:
                    print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}, Checkout Date: {checkout['checkout_date']}")
        except Exception as e:
            print(f"Error listing checkouts: {e}")

    def search_checkout(self, key, value):
        """Search for a checkout transaction based on a key and value.

        Args:
        - key (str): The key to search for (user_id/isbn/checkout_date).
        - value (str): The value to search for.
        """
        try:
            found = False
            for checkout in self.checkouts:
                if str(checkout[key]) == value:
                    print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}, Checkout Date: {checkout['checkout_date']}")
                    found = True
            if not found:
                print("Checkout not found.")
        except Exception as e:
            print(f"Error searching for checkout: {e}")
    
    def list_checkins(self):
        """List all checkins."""
        try:
            if not self.checkins:
                print("No checkins found.")
            else:
                for checkin in self.checkins:
                    print(f"User ID: {checkin['user_id']}, ISBN: {checkin['isbn']}, Checkin Date: {checkin['checkin_date']}")
        except Exception as e:
            print(f"Error listing checkins: {e}")

    def checkout_book(self, user_id, isbn):
        try:
            book_manager = BookManager("data/books.json")
            book = book_manager.get_book(isbn)
            if not book_manager.is_isbn_unique(isbn):
                if book["availability"]:
                    checkout_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    checkout = {"user_id": user_id, "isbn": isbn, "checkout_date": checkout_date}
                    self.checkouts.append(checkout)
                    self.save_checkouts()
                    book_manager.update_book(isbn, availability=False)
                    print("Book checked out successfully.")
                else:
                    print("Book is not available for checkout.")
            else:
                print("Book with ISBN not found.")
        except Exception as e:
            print(f"Error checking out book: {e}")

    def checkin_book(self, user_id, isbn):
        """Checkin a book.

        Args:
        - user_id (str): The ID of the user checking in the book.
        - isbn (str): The ISBN of the book to be checked in.
        """
        try:
            book_manager = BookManager("data/books.json")
            found = False
            for checkout in self.checkouts:
                if checkout["user_id"] == user_id and checkout["isbn"] == isbn:
                    self.checkouts.remove(checkout)
                    self.save_checkouts()
                    book_manager.update_book(isbn, availability=True)
                    print("Book checked in successfully.")
                    found = True
                    break
            if not found:
                print("No matching checkout found.")
        except Exception as e:
            print(f"Error checking in book: {e}")
            
    def checkin_book(self, user_id, isbn):
        """Checkin a book.

        Args:
        - user_id (str): The ID of the user checking in the book.
        - isbn (str): The ISBN of the book to be checked in.
        """
        try:
            book_manager = BookManager("data/books.json")
            found = False
            for checkout in self.checkouts:
                if checkout["user_id"] == user_id and checkout["isbn"] == isbn:
                    self.checkouts.remove(checkout)
                    self.save_checkouts()
                    checkin_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    checkin = {"user_id": user_id, "isbn": isbn, "checkin_date": checkin_date}
                    self.checkins.append(checkin)
                    self.save_checkins()
                    book_manager.update_book(isbn, availability=True)
                    print("Book checked in successfully.")
                    found = True
                    break
            if not found:
                print("No matching checkout found.")
        except Exception as e:
            print(f"Error checking in book: {e}")
    def exit(self):
        """Save data to files before exiting."""
        self.save_checkouts()
        self.save_checkins()
if __name__ == "__main__":
    checkouts_file = "data/checkouts.json"
    checkins_file = "data/checkins.json"
    checkout_manager = CheckManager(checkouts_file)
    checkin_manager = CheckManager(checkins_file)

