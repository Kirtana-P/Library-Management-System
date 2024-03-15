# user.py
from models import User
import storage

"""
Manages the user operations in the library.
"""
class UserManager:

    """Initialize the UserManager with the given storage file.
    Args:
    - storage_file (str): The file path to store user data.
    """
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.users = storage.load_data(storage_file)

    """Save the current user data to the storage file."""
    def save_users(self):
        try:
            storage.save_data(self.storage_file, self.users)
        except Exception as e:
            print(f"Error saving users: {e}")

    """Add a new user to the library.
    Args:
    - name (str): The name of the user.
    - user_id (int): The unique ID of the user.
    """
    def add_user(self, name, user_id):
        try:
            if self.is_user_id_unique(user_id):
                user = {"name": name, "user_id": user_id}
                self.users.append(user)
                self.save_users()
                print("User added successfully")
            else:
                print(f"User with ID {user_id} already exists. Please choose a different ID.")
        except Exception as e:
            print(f"Error adding user: {e}")

    """Check if the user ID is unique.
    
    Args:
    - user_id (str): The user ID to check.
    """
    def is_user_id_unique(self, user_id):
        for user in self.users:
            if user["user_id"] == user_id:
                return False
        return True

    """Update the information of a user in the library.
    Args:
    - user_id (int): The user ID of the user to update.
    - **kwargs: Any attributes of the user to update and their new values.
    """
    def update_user(self, user_id, **kwargs):
        try:
            updated = False
            for user in self.users:
                if user['user_id'] == user_id:
                    for key, value in kwargs.items():
                        if key in ['username']:
                            user[key] = value
                            updated = True
                    # If any attributes are updated, save the changes to the storage file
                    if updated:
                        self.save_users()
                        print(f"User with ID {user_id} updated successfully.")
                    else:
                        print(f"No attributes updated for user with ID {user_id}.")
                    break

            if not updated:
                print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"Error updating user: {e}")

    """Delete a user from the library.
    Args:
    - user_id (int): The user ID of the user to delete.
    """
    def delete_user(self, user_id):
        try:
            self.users = [user for user in self.users if user['user_id'] != user_id]
            self.save_users()
        except Exception as e:
            print(f"Error deleting user: {e}")

    """List all users in the library."""
    def list_users(self):
        try:
            for user in self.users:
                print(f"Name: {user['name']}, User ID: {user['user_id']}")
        except Exception as e:
            print(f"Error listing users: {e}")

    """Search for a user in the library based on a specific attribute.
    Args:
    - key (str): The attribute to search on (e.g., 'name', 'user_id').
    - value: The value to search for in the specified attribute.
    """
    def search_user(self, key, value):
        try:
            found = False
            for user in self.users:
                if user.get(key) == value:
                    print(f"Name: {user['name']}, User ID: {user['user_id']}")
                    found = True
            if not found:
                print("User not found.")
        except Exception as e:
            print(f"Error searching user: {e}")

    def get_user(self, user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                return user
        return None