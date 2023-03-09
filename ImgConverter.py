from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog as fd
import shutil

# TODO:
# - Fix up UI
#   - Add box to tell user the status of the program
#   - Move image to the right?
#   - Make it look good
# - Skip over files that are not images (currently errors on non-image files) (Finished, 3/8)
# - Counter for files checked out of total files (i.e. 24/45)
# - Create error handling
# - Clean up files, split where necessary

window = tk.Tk()
window.title("Image Converter")
window.geometry("950x850+550+100")

# Globals for settings
output_folder = os.getcwd() + "/"
removed_folder = os.getcwd() + "/removed"
end_type = ".png"
delete_file = False
file_count = 0
command = 0
# 0 = Whole folder
# 1 = Single image
# 2 = Whole directory

def show_image(img, canvas):

    # Getting into canvas stuff for image preview at the bottom
    # Get the newly saved image, resize it for preview
    resized_img = img.resize((400, 350))
    # Declare temp as global, otherwise garbage collection removes the image before it can be displayed
    # Convert to PhotoImage for canvas to use
    global temp
    temp = ImageTk.PhotoImage(resized_img)
    # Place image at 0,0, update canvas to display. Convert the resized image into a PhotoImage
    canvas.create_image(0,0,anchor=tk.NW, image=temp)
    canvas.update()

def convert_img(canvas, path):
    # Splits path into tuple. [0] = Path, [1] = File
    # Ex: /Desktop/Images/img.png
    # [0] = /Desktop/Images, [1] = img.png
    #print("FULL PATH: ", path)
    path_tuple = os.path.split(path)

    # Separating the file name and its extension
    # Ex: [0] = img, [1] = .png
    filename_tuple = os.path.splitext(path_tuple[1])

    # Ex: /Desktop/Images + img + .jpg
    converted_path = path_tuple[0] + "/" + filename_tuple[0] + end_type

    try:
        img = Image.open(path)
        show_image(img, canvas)
    except Exception as e:
        #print(e)
        print("[X] File: ", path_tuple[1], " is not an applicable type to convert. Skipping...")
        return

    if filename_tuple[1] == end_type:
        print("[~] Skipping: ", path_tuple[1], ", already in desired type...")
        return
    elif os.path.exists(converted_path):
        print("[~] File: ", path_tuple[1], " already exists in desired type. Moving old file...")
        os.rename(path, os.getcwd() + "/removed")
        print("[-] Old file removed. Continuing...")
        return
    else:
        print("[+] Saving ", path_tuple[1], " as: ", end_type)
        img.save(path + filename_tuple[0] + end_type)

        print("[-] Removing old file: ", path_tuple[1], "...")
        shutil.move(path, removed_folder)
        print("[~] Done. Continuing...")
        return

# Temp function before adding more options for file manipulation
def temp_run(canvas, folder):
    for file in os.listdir(folder):
        convert_img(canvas, folder+"/"+file)


label_frame = tk.Frame(master=window, width=75, height=50)
file_button_frame = tk.Frame(master=window, width=75, height=5)
file_path_frame = tk.Frame(master=window, width=75, height=5)
output_text_frame = tk.Frame(master=window, width=75, height=5)
output_button_frame = tk.Frame(master=window, width=75, height=5)
run_button_frame = tk.Frame(master=window, width=75, height=5)
img_frame = tk.Frame(master=window, width=75, height=25)
canvas_frame = tk.Frame(master=window, width=75, height=25)

entry_text= ""
output_text = ""

canvas = tk.Canvas(canvas_frame, width=400, height=350)

def get_file(file_path):
    file = fd.askdirectory()
    file_path.delete(0, tk.END)
    file_path.insert(0, file+"/")


greeting_label = tk.Label(
    master=label_frame,
    text="Please choose which folder to work in.",
    width=75,
    height=10,
    bg="white",
    justify="left"
).pack()

input_folder_button = tk.Button(
    master=file_button_frame,
    text="Choose folder...",
    relief= tk.RAISED,
    width=75,
    height=5,
    command=lambda: get_file(input_file_path)
    #bg="blue"
)

input_file_path = tk.Entry(
    master=file_path_frame,
    width=75,
    textvariable=entry_text
    #height=5
)

output_folder_button = tk.Button(
    master=output_button_frame,
    text="Choose output folder...",
    relief=tk.RAISED,
    width=75,
    height=5,
    command=lambda: get_file(output_file_path)
)

output_file_path = tk.Entry(
    master=output_text_frame,
    width=75,
    textvariable=output_text
)

run_button = tk.Button(
    master=run_button_frame,
    text="Run",
    relief=tk.RAISED,
    width=75,
    height=5,
    command=lambda: temp_run(canvas, input_file_path.get())
)


img_label = tk.Label(
    master=img_frame,
    #image=None,
    width=0,
    height=0,
)

input_folder_button.pack()
input_file_path.pack()
output_folder_button.pack()
output_file_path.pack()
run_button.pack()
img_label.pack()
canvas.pack()

label_frame.pack(fill=tk.BOTH)
file_button_frame.pack(fill=tk.BOTH)
file_path_frame.pack(fill=tk.BOTH)
output_button_frame.pack(fill=tk.BOTH)
output_text_frame.pack(fill=tk.BOTH)
run_button_frame.pack(fill=tk.BOTH)
img_frame.pack(fill=tk.BOTH)
canvas_frame.pack(fill=tk.BOTH)


window.mainloop()
