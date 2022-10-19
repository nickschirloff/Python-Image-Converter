from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog as fd
import stat

# TODO:
# - Fix up UI
#   - Add box to tell user the status of the program
#   - Move image to the right?
#   - Make it look good
# - Skip over files that are not images (currently errors on non-image files)
# - Counter for files checked out of total files (i.e. 24/45)
# - Clean up files, split where necessary


window = tk.Tk()
window.title("Image Converter")
window.geometry("650x850+550+100")

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

def convert_images(folder, canvas):
    count = 0
    try:
        # Run through each file in directory
        for filename in os.listdir(folder):
            
            # Initialize the image
            img = Image.open(folder + filename)

            # Get the last 5 characters of the filename, check if its a .webp file
            file_type = filename[len(filename)-5:len(filename)]
            if file_type.lower() != ".webp":
                show_image(img, canvas)
                print("[~] File", filename, "is not a .webp. Continuing...")
                continue

            # Create temporary variable to hold the path of the file, minus the .webp characters
            temp = folder + filename[0:len(filename)-5]
            #print("Temp:", temp)
            
            # Make sure that the image is not already converted into a .png within the folder
            if os.path.exists(temp + ".png"):
                show_image(img, canvas)
                print("[-] File", filename, "is already a .png in designated folder. Removing the .webp...")
                # Giving program permission to delete files
                os.chmod(folder+filename, 0o777)
                os.remove(folder + filename)
                print("[-] Removed", folder + filename, ". Continuing...")
                continue
            

            print("[+] Saving", filename, "as:", temp + ".png")
            # Resave the image, convert to png
            img.save(temp + ".png")

            temp_img = Image.open(temp + ".png")
            show_image(temp_img, canvas)
            #temp_img = ImageTk.PhotoImage(resized_img)
            #canvas.create_image(0,0, anchor=tk.NW, image=temp_img)

            # Remove old .webp file from folder (Maybe make this a checkbox option later)
            print("[-] Removing: ", folder + filename)
            os.chmod(folder+filename, 0o777)
            os.remove(folder + filename)
            
            count += 1
            print("Successfully converted .webp. Total:", count)
    except Exception as e:
        print(e)
    print("Finished converting.")


label_frame = tk.Frame(master=window, width=75, height=50)
file_button_frame = tk.Frame(master=window, width=75, height=5)
file_path_frame = tk.Frame(master=window, width=75, height=5)
run_button_frame = tk.Frame(master=window, width=75, height=5)
img_frame = tk.Frame(master=window, width=75, height=25)
canvas_frame = tk.Frame(master=window, width=75, height=25)

entry_text= ""

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
    bg="white"
).pack()

img_label = tk.Label(
    master=img_frame,
    #image=None,
    width=0,
    height=0,
)

file_path = tk.Entry(
    master=file_path_frame,
    width=75,
    textvariable=entry_text
    #height=5
)

button = tk.Button(
    master=file_button_frame,
    text="Choose folder...",
    relief= tk.RAISED,
    width=75,
    height=5,
    command=lambda: get_file(file_path)
    #bg="blue"
)

run_button = tk.Button(
    master=run_button_frame,
    text="Run",
    relief=tk.RAISED,
    width=75,
    height=5,
    command=lambda: convert_images(file_path.get(), canvas)
)


button.pack()
file_path.pack()
run_button.pack()
img_label.pack()
canvas.pack()

label_frame.pack(fill=tk.BOTH)
file_button_frame.pack(fill=tk.BOTH)
file_path_frame.pack(fill=tk.BOTH)
run_button_frame.pack(fill=tk.BOTH)
img_frame.pack(fill=tk.BOTH)
canvas_frame.pack(fill=tk.BOTH)


window.mainloop()