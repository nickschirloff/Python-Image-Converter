from PIL import Image
import os
import shutil

class Convert:

    config = {}
    frame = None
    total_file_count = 0

    def __init__(self, config, frame):
        self.config = config
        self.frame = frame
        self.current_file_count = 0
        

    def convert_img(self, path):
        # Splitting path into a tuple. [0] = Path, [1] = File
        # Ex: /Desktop/Images/img.png
        # [0] = /Desktop/Images/, [1] = img.png
        path_tuple = os.path.split(path)

        # Separating file name and file extension
        # Ex: [0] = img, [1] = .png
        filename_tuple = os.path.splitext(path_tuple[1])

        new_path = path_tuple[0] + "/" + filename_tuple[0] + self.config.get("end_type")

        try:
            img = Image.open(path)
            self.frame.show_image(img)

            if filename_tuple[1] == self.config.get("end_type"):
                print("[~] File: ", path_tuple[1], " is already in desired format. Skipping...")
                return
            elif os.path.exists(new_path):
                print("[~] File: ", path_tuple[1], " already exists. Skipping...")
            else:
                print("[+] Saving: ", path_tuple[1], " as: ", self.config.get("end_type"))
                img.save(new_path)
                print("[>] Done. Continuing...")

            if(self.config.get("delete_flag") == "True"):
                print("[-] Removing:", path_tuple[1], "...")
                shutil.move(path,self.config.get("removed_folder"))
                print("[>] Done. Continuing...")
            self.update_file_count(self.total_file_count)
            return
        except Exception as e:
            print("[X] File: ", path_tuple[1], " is not able to be converted. Skipping...")
            print(e)
            return
        
    def convert_folder(self, path, label):
        for file in os.listdir(path):
            total_file_count = self.get_file_count(path)
            #self.current_file_count = self.current_file_count + 1
            #label = str(self.current_file_count)
            self.convert_img(path+file)

    def get_file_count(self, path):
        total_file_count = len([name for name in os.listdir(path)])
        self.total_file_count = total_file_count
        return total_file_count

    def update_file_count(self, num):
        self.current_file_count = self.current_file_count + 1
        print("Update: ", self.current_file_count)
        self.frame.current_file_count.set(str(self.current_file_count) + "/" + str(num))
    
    def get_op(self, command, path, label):
        match command:
            case "0": # Convert entire folder
                return self.convert_folder(path, label)
            case "1": # Convert singular image
                return self.convert_img(path, label)
