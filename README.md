# JSON Utils

A lightweight Python utility library that simplifies loading, editing, and saving JSON configuration files.

## Features

- Load JSON files into Python dictionaries
- Edit nested JSON values using a path list
- Automatically save changes to the file
- Basic file validation and error handling

## Example JSON File

```json
{
    "data_set_one": {
        "vari_one": "True",
        "vari_two": "True",
        "vari_three": "True"
    },
    "data_set_two": {
        "vari_one": "False",
        "vari_two": "False",
        "vari_three": "False"
    }
}
```

## Example Usage

```python
# Import the json_utils module
import json_utils

# Specify the JSON file you want to work with.
# The file should be located in the same directory as this script.
filename = "example_config.json"

# Generate the full file path for the JSON file.
file_directory = json_utils.get_directory(filename)

# Load the JSON file into a Python variable.
data = json_utils.load_file(file_directory)

# Define the path to the value you want to modify.
path = ["data_set_one", "vari_one"]

# Set the new value that will replace the current value.
new_value = "False"

# Apply the change and save the updated JSON file.
json_utils.change_data(data, path, new_value, file_directory)
```

## Available Functions

### `get_directory(filename)`

Returns the absolute path to a file located in the same directory as the module.

```python
file_directory = json_utils.get_directory(
    "example_config.json"
)
```

### `load_file(file_directory)`

Loads a JSON file and returns its contents as a Python dictionary.

```python
data = json_utils.load_file(file_directory)
```

### `change_data(data, path, new_value, file_directory)`

Updates a value within the JSON data and saves the changes back to the file.

```python
json_utils.change_data(
    data,
    ["data_set_one", "vari_one"],
    "False",
    file_directory
)
```

## Understanding Paths

A path is a list of keys that leads to the value you want to modify.

Example JSON:

```json
{
    "settings": {
        "audio": {
            "volume": 75
        }
    }
}
```

Path to `volume`:

```python
["settings", "audio", "volume"]
```

Example update:

```python
json_utils.change_data(
    data,
    ["settings", "audio", "volume"],
    50,
    file_directory
)
```

## Error Handling

The library includes checks for:

- Missing files
- Empty files
- File permission issues

## Future Improvements

- Add support for creating new keys
- Add support for deleting keys
- Improve exception handling
- Add type hints
- Add automated tests

## Author

Created as a personal Python project to simplify working with JSON configuration files.
