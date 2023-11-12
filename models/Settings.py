import json
import os

def read_settings():
    try:
        path = os.getcwd()
        path += "\\resources\\config.json"

        # Creating a settings file if it does not exist
        if not(os.path.exists(path)):
            json_string = '{"last_folder":"", "end_type":".png", "delete_flag":"False", "remove_path":"./removed"}'
            with open(path, "x") as f:
                json.dump(json_string, f, indent=4)

        with open(path, 'r') as f:
            config = json.loads(f.read())
            print(config.get("end_type"))
            return config
    except Exception as e:
        print("Error reading settings json. Details:")
        print(e)

def write_settings(settings):
    try:
        path = os.getcwd()
        path += "\\resources\\config.json"

        # Creating a settings file if it does not exist
        if not(os.path.exists(path)):
            json_string = '{"last_folder":"", "end_type":".png", "delete_flag":"False", "remove_path":"./removed"}'
            with open(path, "x") as f:
                json.dumps(json_string, f, indent=4)
    except Exception as e:
        print("Error writing settings to json. Details:")
        print(e)
