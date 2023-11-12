import os
import shutil
from PIL import Image

class ConvertImage:
    def __init__(self, update_panel):
        # Load settings here
        self.update_panel = update_panel
        self.file_count = 1
        self.total_file_count = 0

    def convert_folder(self, dir):
        self.total_file_count = len([name for name in os.listdir(dir)])
        for file in os.listdir(dir):
            self.convert_image(dir + "/" + file)
            self.file_count += 1

    def convert_image(self, path):
        # [0] = /Path/To/Image/  [1] = img.webp
        path_tuple = os.path.split(path)
        # [0] = img  [1] = .webp
        filename_tuple = os.path.splitext(path_tuple[1])
        # TODO: Convert below line to read from config json
        new_path = path_tuple[0] + "/" + filename_tuple[0] + ".png"

        # TODO: Convert below line to read from config json
        remove_path = os.getcwd() + "/removed"
        if not(os.path.exists(remove_path)):
            os.mkdir(remove_path)
        
        try: 
            img = Image.open(path)

            self.update_panel(path, filename_tuple[0], "%s/%s" % (str(self.file_count), str(self.total_file_count)))
            # TODO: Convert below line to read from config json
            if(filename_tuple[1] == ".png"):
                print("[~] File: ", path_tuple[0] + " is already in desired format. Skipping...")
                return False
            elif(os.path.exists(new_path)):
                print("[~] File: " + path_tuple[0] + " already exists. Skipping...")
                return False
            else:
                # TODO: Convert below line to read from config json
                print("[+] Converting: " + path_tuple[1] + " to " + ".png" + "...")
                img.save(new_path)
                print("[>] Done. Continuing...")
                

            # TODO: Convert below line to read from config json 
            if("True" == "True"):
                print("[-] Removing: " + path_tuple[1] + "...")
                # TODO: Convert below line to read from config json
                shutil.move(path, os.getcwd() + "\\removed\\")
                print("[>] Done. Continuing...")
            
            return True
        except Exception as e:
            print("[*] File: " + filename_tuple[1] + " is not able to be converted. Continuing...")
            print("    If this is not expected behavior, check error code below:")
            print(e)
            return False
