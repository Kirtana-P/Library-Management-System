from book import BookManager
from user import UserManager
from check import CheckManager

books_file = "data/books.json"
users_file = "data/users.json"
checkouts_file = "data/checkouts.json"
checkins_file = "data/checkins.json"

# Initialize managers with default data
book_manager = BookManager(books_file)
user_manager = UserManager(users_file)
checkout_manager = CheckManager(checkouts_file)
checkin_manager = CheckManager(checkins_file)

# Function to add a new book to the library
def add_book(book_manager):
    try:
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        if book_manager.is_isbn_unique(isbn):
            book_manager.add_book(title, author, isbn)
            print("\nBook added successfully.")
        else:
            print(f"A book with ISBN {isbn} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to update information of a book
def update_book(book_manager):
    try:
        isbn = input("Enter ISBN of the book to update: ")
        title = input("Enter new title (leave empty to keep current): ")
        author = input("Enter new author (leave empty to keep current): ")
        if title or author:
            book_manager.update_book(isbn, title=title, author=author)
        else:
            print("No changes made.")
    except Exception as e:
        print(f"An error occurred: {e}")



# Function to delete a book from the library
def delete_book(book_manager):
    try:
        isbn = input("Enter ISBN of the book to delete: ")
        book_manager.delete_book(isbn)
        print("Book with ISBN has been deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to list all books in the library
def list_books(book_manager):
    try:
        book_manager.list_books()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search for a book in the library
def search_book(book_manager):
    try:
        key = input("Enter search key (title/author/isbn): ")
        value = input("Enter search value: ")
        books = book_manager.search_book(key, value)
        if not books:
            print("No books found.")
        else:
            for book in books:
                availability = "Available" if book["availability"] else "Not Available"
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Availability: {availability}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to add a new user to the library
def add_user(user_manager):
    try:
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        user_manager.add_user(name, user_id)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to update information of a user
def update_user(user_manager):
    try:
        user_id = input("Enter user ID to update: ")
        new_username = input("Enter new username: ")
        user_manager.update_user(user_id, username=new_username)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to delete a user from the library
def delete_user(user_manager):
    try:
        user_id = input("Enter user ID to delete: ")
        user_manager.delete_user(user_id)
        print("User deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to list all users in the library
def list_users(user_manager):
    try:
        user_manager.list_users()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search for a user in the library
def search_user(user_manager):
    try:
        key = input("Enter search key (name/user_id): ")
        value = input("Enter search value: ")
        user_manager.search_user(key, value)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to checkout a book
def checkout_book(checkout_manager):
    try:
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        checkout_manager.checkout_book(user_id, isbn)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to checkin a book
def checkin_book(checkout_manager):
    try:
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkin: ")
        checkout_manager.checkin_book(user_id, isbn)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to list all checkout transactions
def list_checkouts(checkout_manager):
    try:
        checkout_manager.list_checkouts()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search for a checkout transaction
def search_checkout(checkout_manager):
    try:
        key = input("Enter search key (user_id/isbn/checkout_date): ")
        value = input("Enter search value: ")
        checkout_manager.search_checkout(key, value)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to list all checkins
def list_checkins(checkout_manager):
    try:
        checkout_manager.list_checkins()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search for a checkin transaction
def search_checkin(checkout_manager):
    try:
        key = input("Enter search key (user_id/isbn/checkin_date): ")
        value = input("Enter search value: ")
        checkout_manager.search_checkin(key, value)
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the library management system
def main():
    book_manager = BookManager("data/books.json")
    user_manager = UserManager("data/users.json")
    checkout_manager = CheckManager("data/checkouts.json")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search Book")
        print("6. Add User")
        print("7. Update User")
        print("8. Delete User")
        print("9. List Users")
        print("10. Search User")
        print("11. Checkout Book")
        print("12. Checkin Book")
        print("13. List Checkouts")
        print("14. Search Checkout")
        print("15. List Checkins")
        print("16. Search Checkin")
        print("17. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_book(book_manager)

        elif choice == '2':
            update_book(book_manager)

        elif choice == '3':
            delete_book(book_manager)

        elif choice == '4':
            list_books(book_manager)

        elif choice == '5':
            search_book(book_manager)

        elif choice == '6':
            add_user(user_manager)

        elif choice == '7':
            update_user(user_manager)

        elif choice == '8':
            delete_user(user_manager)

        elif choice == '9':
            list_users(user_manager)

        elif choice == '10':
            search_user(user_manager)

        elif choice == '11':
            checkout_book(checkout_manager)

        elif choice == '12':
            checkin_book(checkout_manager)

        elif choice == '13':
            list_checkouts(checkout_manager)

        elif choice == '14':
            search_checkout(checkout_manager)
            
        elif choice == '15':
            list_checkins(checkin_manager)

        elif choice == '16':
            search_checkin(checkin_manager)

        elif choice == '17':
            checkout_manager.exit()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
