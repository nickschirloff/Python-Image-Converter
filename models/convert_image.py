from PIL import Image
import shutil
import os

class ConvertedImage:
    def __init___(self, path, config):
        self.path = path
        self.config = config
        # [0] = /Path/To/Image/  [1] = img.webp
        self.path_tuple = os.path.split(path)
        # [0] = img  [1] = .webp
        self.filename_tuple = os.path.splitext(self.path_tuple[1])

    def do_conversion(self):
        new_path = self.path_tuple[0] + "/" + self.filename_tuple[1] + self.config.get("end_type")

        try:
            img = Image.open(self.path)

            if(self.filename_tuple[1] == self.config.get("end_type")):
                print("[~] File: ", self.path_tuple[1] + " is already in desired format. Skipping...")
                return False
            elif(os.path.exists(new_path)):
                print("[~] File: " + self.path_tuple[1] + " already exists. Skipping...")
                return False
            else:
                print("[+] Converting: " + self.path_tuple[1] + " to " + self.config.get("end_type") + "...")
                img.save(new_path)
                print("[>] Done. Continuing...")

            if(self.config.get("delete_flag") == "True"):
                print("[-] Removing: " + self.path_tuple[1] + "...")
                shutil.move(self.path, self.config.get("removed_path"))
                print("[>] Done. Continuing...")
            
            return True
        except Exception as e:
            print("[*] File: " + self.file_tuple[1] + " is not able to be converted. Continuing...")
            print("    If this is not expected behavior, check error code below:")
            print(e)
            return False
