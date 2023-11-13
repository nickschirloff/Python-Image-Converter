import json
import os

def read_settings():
    '''
    Read settings from config json
    
    Parameters:
    none
    Returns:
    config (dict): A dict containing saved settings
    '''
    try:
        path = os.getcwd()
        path += "\\resources\\config.json"

        # Generate a settings file if it does not exist
        if not(os.path.exists(path)):
            with open(path, "x") as f:
                json.dump(generate_default_settings(), f)

        with open(path, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        print("Error reading settings json. Details:")
        print(e)

def write_settings(settings):
    '''
    Write settings to json file
    
    Parameters:
    settings (dict): The json to write to settings
    Returns:
    none
    '''
    try:
        path = os.getcwd()
        path += "\\resources\\config.json"

        # Creating a settings file if it does not exist
        if not(os.path.exists(path)):
            with open(path, "x") as f:
                json.dump(settings, f)
        else:
            with open(path, "w") as f:
                json.dump(settings, f)
    except Exception as e:
        print("Error writing settings to json. Details:")
        print(e)

''' Return default settings json '''
def generate_default_settings():
    return {
                "last_folder": "",
                "end_type": ".png",
                "delete_flag": "True",
                "remove_path": os.getcwd() + "\\removed"
    }