import os
import json

def main():
    file_diretory = os.getcwd() + "\\exampleconfig.json"
    test_errors(file_diretory)

    data = load_file(file_diretory)
    print(f"Current Data: {data}")


def test_errors(file_diretory):
        try:
            os.access(file_diretory, os.F_OK | os.R_OK)
        except PermissionError:
            print(f"Invalid Permissions For: {file_diretory}")
            exit()
        except FileNotFoundError:
            print(f"Could Not Find File: {file_diretory}")
            exit()



def load_file(file_directory):
     if os.path.getsize(file_directory) == 0:
          print(f"File: {file_directory} is empty")
          exit()
     with open(file_directory, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def change_data(data):
     0


'''
def change_data(data):

def close_file():


if 'key' in data:
    data['key'] = 'new_value'

# Example: Replace a nested value
if 'parent' in data and 'child' in data['parent']:
    data['parent']['child'] = 'new_nested_value'

# 3. Write back to the same file
with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)



'''
main()
