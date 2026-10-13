# import the json_utils file
import json_utils 

# Specify the JSON file you want to work with.
# The file should be located in the same directory as this script.
filename = "\\example_config.json"

# Generate the full file path for the JSON file.
file_directory = json_utils.get_directory(filename)

# Load the JSON file into a Python variable.
data = json_utils.load_file(file_directory)

# Define the path to the value you want to modify.
path = ["data_set_one", "vari_one"]

# Set the new value that will replace the current value.
new_value = "False"


json_utils.change_data(data, path, new_value, file_directory)
