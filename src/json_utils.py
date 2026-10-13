import os
import json

def get_directory(filename):
    file_directory = os.path.dirname(os.path.abspath(__file__)) + filename
    return file_directory

def load_file(file_directory):
    try:
        os.access(file_directory, os.F_OK | os.R_OK)
        if os.path.getsize(file_directory) == 0:
            print(f"File: {file_directory} is empty")
            exit()
        with open(file_directory, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except PermissionError:
        print(f"Invalid Permissions For: {file_directory}")
        exit()
    except FileNotFoundError:
        print(f"Could Not Find File: {file_directory}")
        exit()

def change_data(data, path, new_value, file_directory):
    current = data
    for key in path[:-1]:
        current = current[key]
    current[path[-1]] = new_value
    with open(file_directory, 'w') as f:
        json.dump(data, f, indent=4)
