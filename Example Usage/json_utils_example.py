# import the json_utils file
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

# Apply the change and write the updated data to the JSON file.
json_utils.change_data(path, new_value, file_directory)
