from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog as fd

window = tk.Tk()
window.title("Image Converter")
window.geometry("650x850+550+100")

def convert_pictures(folder, canvas):
    count = 0
    print("Folder: ", folder)
    try:
        # Run through each file in directory
        for filename in os.listdir(folder):
            img = Image.open(folder + filename)
            resized_img = img.resize((400,350), Image.ANTIALIAS)
            temp_img = ImageTk.PhotoImage(resized_img)
            canvas.create_image(0, 0, anchor=tk.NW, image=temp_img)
            canvas.update()
            # Get the file type of the current file
            # We get the last five characters of the file to see if it is a .webp
            file_type = filename[len(filename)-5:len(filename)]
            # Create variable to hold full path of file, minus the extension
            temp = folder + filename[0:len(filename)-4]
            # Finally, check that file type is .webp, and make sure it doesn't already exist as a .png
            if file_type == ".webp" and not os.path.exists(temp+".png"):
                # Open image, re-save it with the
                
                temp = folder + filename[0:len(filename)-4]
                print("Saving", filename, " as: ", temp+".png")
                # Add new file extension to image
                img.save(temp + ".png")
                # Remove old .webp from the folder
                print("Removing: ", folder+filename)
                os.remove(folder+filename)
                count += 1
                print("Found .webp file. Total: ", count)
            else:
                print("Continuing...")
                continue

    except:
        print("Failed")
    print("Finished.")



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

def convert_images(folder, canvas):
    convert_pictures(folder, canvas)


greeting_label = tk.Label(
    master=label_frame,
    text="Please choose which folder to work in.",
    width=75,
    height=10,
    bg="white"
).pack()

img_label = tk.Label(
    master=img_frame,
    image=None,
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