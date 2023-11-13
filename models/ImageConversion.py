import os
import shutil
from PIL import Image
from models.Settings import read_settings

class ConvertImage:
    def __init__(self, update_panel):
        self.update_panel = update_panel
        self.file_count = 1
        self.total_file_count = 0
        self.config = read_settings()

    def convert_folder(self, dir):
        '''
        Iterates over a folder to attempt to convert image types
        
        Parameters:
        dir (str): The directory to iterate over
        Returns:
        none
        '''
        if not(os.path.isdir(dir)):
            print("[*] Error: Input directory does not exist. Please double check that the path is correct")
            return
        
        self.total_file_count = len([name for name in os.listdir(dir)])
        if(self.total_file_count == 0):
            print("[*] No files in directory specified. Make sure you have the correct directory and try again.")
            return
        
        for file in os.listdir(dir):
            fp = dir + file
            self.convert_image(fp)
            self.file_count += 1
        print("Finished.")
        return
    
    def convert_image(self, path):
        '''
        Convert a singular image into the desired 
    
        Parameters:
        path (str): The path to the image
        Returns:
        True: Image was converted successfully
        False: Image could not be converted
        '''
        # [0] = /Path/To/Image/  [1] = img.webp
        path_tuple = os.path.split(path)
        # [0] = img  [1] = .webp
        filename_tuple = os.path.splitext(path_tuple[1])
        new_path = path_tuple[0] + "/" + filename_tuple[0] + self.config.get("end_type")

        temp = self.config.get("remove_path")
        if (temp == "" or temp == "/removed") and not(os.path.exists(os.getcwd() + "/removed")):
            os.mkdir(os.getcwd() + "/removed")
        
        try: 
            img = Image.open(path)

            self.update_panel(path, filename_tuple[0], "%s/%s" % (str(self.file_count), str(self.total_file_count)))
            if(filename_tuple[1] == self.config.get("end_type")):
                print("[~] File: ", path_tuple[0] + " is already in desired format. Skipping...")
                return False
            elif(os.path.exists(new_path)):
                print("[~] File: " + path_tuple[0] + " already exists. Skipping...")
                return False
            else:
                print("[+] Converting: " + path_tuple[1] + " to " + self.config.get("end_type") + "...")
                img.save(new_path)
                print("[>] Done. Continuing...")
                
            if(self.config.get("delete_flag") == "True"):
                print("[-] Removing: " + path_tuple[1] + "...")
                shutil.move(path, os.getcwd() + "\\removed\\")
                print("[>] Done. Continuing...")
            
            return True
        except Exception as e:
            print("[*] File: " + filename_tuple[1] + " is not able to be converted. Continuing...")
            print("    If this is not expected behavior, check error code below:")
            print(e)
            return False
