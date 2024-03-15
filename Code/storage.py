#storage.py
"""
Provides functions for saving and loading data using JSON format.
"""
import json
import os

def save_data(filename, data):
    """Save data to a file in JSON format.
    Args:
    - filename (str): The file path to save the data to.
    - data (dict or list): The data to be saved.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_data(filename):
    """Load data from a file in JSON format.
    If the file does not exist, create it with an empty list.
    Args:
    - filename (str): The file path to load the data from.
    Returns:
    - dict or list: The loaded data.
    """
    try:
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([], file)
            return []
        
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")
        return []

def update_data(filename, data):
    """Update existing data in a file with new data.
    Args:
    - filename (str): The file path to update the data in.
    - data (dict or list): The new data to be added.
    """
    current_data = load_data(filename)
    current_data.append(data)
    save_data(filename, current_data)

def save_checkins(data):
    """
    Save check-in data to a JSON file.
    Args:
    - data (list): The check-in data to be saved.
    """
    with open("checkins.json", "w") as file:
        json.dump(data, file, indent=4)

def load_checkins():
    """
    Load check-in data from a JSON file.
    Returns:
    - list: The loaded check-in data.
    """
    try:
        with open("checkins.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  
    except Exception as e:
        print(f"Error loading check-ins data: {e}")
        return []