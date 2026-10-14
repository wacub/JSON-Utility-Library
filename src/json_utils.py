import os
import json

def get_directory(filename):
    file_directory = os.path.dirname(os.path.abspath(__file__)) + "\\" + filename
    return file_directory

def load_file(file_directory):
    try:
        os.access(file_directory, os.F_OK | os.R_OK)
        if os.path.getsize(file_directory) == 0:
            raise ValueError(f"File: {file_directory} is empty")
                    
        with open(file_directory, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
        
    except PermissionError:
        print(f"Invalid Permissions For: {file_directory}")
        
    except FileNotFoundError:
        print(f"Could Not Find File: {file_directory}")

    except ValueError as e:
        print(e)

def change_data(path, new_value, file_directory):
    data = load_file(file_directory)
    current = data

    try:
        for key in path[:-1]:
            current = current[key]

        if path[-1] not in current:
            raise KeyError

        current[path[-1]] = new_value

        print(data)
        with open(file_directory, 'w') as f:
            json.dump(data, f, indent=4)
            f.close()

    except KeyError:
        print(f"Invalid path: {path}")
