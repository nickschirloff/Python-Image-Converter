import json

class Settings:

    def load():
        """
        Load saved settings from settings.json. If unable to, loads default values.

        :return: Dictionary containing previously saved config data, or default data.
        """
        config = {}
        try:
            with open('settings.json', 'r') as s:
                config = json.load(s)
            return config
        except Exception as e:
            print('Unable to open settings file. Loading defaults.')
            print(e)
            return {"output_folder":"/output","removed_folder":"/removed","end_type":".png","delete_flag":"False","command":"0"}

    def write(config):
        """
        Write config settings to settings.json file. Executed after hitting the run button, and writes
        the settings used during the previous run.

        :param dict config: The updated configuration settings to be written to settings.json
        :return: True or false, depending if the settings were saved properly
        """
        try:
            with open('settings.json', 'w') as s:
                json.dump(config)
            return True
        except Exception as e:
            print('Unable to write to settings file. Settings will stay as they were.')
            print(e)
            return False
