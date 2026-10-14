# JSON Utils

A lightweight Python utility library that simplifies loading, editing, and saving JSON configuration files.

## Features

- Load JSON files into Python dictionaries
- Edit nested JSON values using a path list
- Create new JSON entries
- Automatically create missing parent paths when creating entries
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
# Import the json_utils file
import json_utils

# Specify the JSON file you want to work with.
# The file should be located in the same directory as this script.
filename = "example_config.json"

# Generate the full file path for the JSON file.
file_directory = json_utils.get_directory(filename)

# Define the path to the value you want to modify.
path = ["data_set_two", "vari_one"]

# Set the new value that will replace the current value.
new_value = "True"

# Apply the change and save the updated JSON file.
json_utils.change_data(path, new_value, file_directory)

# Set the value that will be assigned to the new entry.
value = "False"

# Define the path where the new entry will be created.
path = ["data_set_three", "vari_one"]

# Create the new entry and save it to the JSON file.
json_utils.create_new_entry(path, value, file_directory)
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

### `change_data(path, new_value, file_directory)`

Updates an existing value in a JSON file and saves the changes.

```python
json_utils.change_data(
    ["data_set_two", "vari_one"],
    "True",
    file_directory
)
```

### `create_new_entry(path, value, file_directory)`

Creates a new entry in the JSON file.

If parent paths do not exist, they will be created automatically.

```python
json_utils.create_new_entry(
    ["data_set_three", "vari_one"],
    "False",
    file_directory
)
```

Result:

```json
{
    "data_set_three": {
        "vari_one": "False"
    }
}
```

## Understanding Paths

A path is a list of keys that leads to the location you want to modify or create.

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

Updating the value:

```python
json_utils.change_data(
    ["settings", "audio", "volume"],
    50,
    file_directory
)
```

Creating a new entry:

```python
json_utils.create_new_entry(
    ["settings", "audio", "mute"],
    False,
    file_directory
)
```

Result:

```json
{
    "settings": {
        "audio": {
            "volume": 50,
            "mute": false
        }
    }
}
```

## Error Handling

The library checks for:

- Missing files
- Empty files
- File permission issues
- Invalid paths when modifying data
- Duplicate entries when creating data


## Future Improvements

- Delete existing entries
- Create new JSON files
- Return status values instead of printing messages
- Add type hints
- Add automated tests
- Improve exception handling

## Author

Created as a personal Python project to simplify working with JSON configuration files.
