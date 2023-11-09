import json
import os

def read_settings():
    # Get path from current directory
    path = os.getcwd()
    path += "\\resources\\config.json"

    # Create settings json if it does not exist
    if not os.path.exists(path):
        json_string = "{'last_folder': '', 'end_type': '.png', 'delete_flag': 'False', 'remove_path': './removed'}"
        with open(path, "x") as file:
            json.dump(json_string, file)
    
    try:
        with open(path, "r") as file:
            config = json.load(file)
    except Exception as e:
        print("Error reading file. Details:")
        print(e)



def write_settings(settings):
    # Get path from current directory
    path = os.getcwd()
    path += "\\resources\\config.json"
    
    try:
        with open(path, "w") as file:
            json.dump(settings, file)
    except Exception as e:
        print("Error writing to json. Details:")
        print(e)
