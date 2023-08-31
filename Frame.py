import tkinter as tk
from tkinter import filedialog as fd
from tkinter import StringVar
from PIL import ImageTk
from SettingsLoader import Settings as st
from ConvertImg import Convert as ct

class Frame():

    WINDOW_WIDTH = 1250
    WINDOW_HEIGHT = 850
    IMAGE_SIZE = 675

    config = st.load()

    def __init__(self, window):

        test = ct(self.config,self)

        self.window = window
        window.title("Image Converter")
        window.geometry(str(self.WINDOW_WIDTH)+"x"+str(self.WINDOW_HEIGHT)+"+100+100")
        
        self.input_path = StringVar()
        self.output_path = StringVar()

        self.current_file_count = StringVar()
        self.total_file_count = StringVar()

        welcome_label = tk.Label(
            master=window,
            text="Please choose which folder to work in:",
            width=70,
            height=5,
            bg="white",
        )
        input_folder_button = tk.Button(
            master=window,
            text="Choose folder...",
            relief=tk.RAISED,
            width=70,
            height=5,
            command=lambda: self.get_file(input_file_path)
        )
        input_file_path = tk.Entry(
            master=window,
            width=70,
            textvariable=self.input_path
        )
        output_folder_button = tk.Button(
            master=window,
            text="Choose output folder...",
            relief=tk.RAISED,
            width=70,
            height=5,
            command=lambda: window.get_file(output_file_path)
        )
        output_file_path = tk.Entry(
            master=window,
            width=70,
            textvariable=self.output_path
        )
        run_button = tk.Button(
            master=window,
            text="Run",
            relief=tk.RAISED,
            width=70,
            height=5,
            command=lambda: test.get_op(self.config.get("command"),input_file_path.get(),self.file_count_label)
        )
        self.file_count_label = tk.Label(
            master=window,
            width=70,
            height=2,
            bg="white",
            textvariable=self.current_file_count
        )
        self.canvas = tk.Canvas(
            master=window,
            width=680,
            height=850,
        )

        welcome_label.grid(row=0,column=0,sticky="nsew")
        input_folder_button.grid(row=1,column=0,sticky="nsew")
        input_file_path.grid(row=2,column=0,sticky="nsew")
        output_folder_button.grid(row=3,column=0,sticky="nsew")
        output_file_path.grid(row=4,column=0,sticky="nsew")
        run_button.grid(row=5,column=0,sticky="nsew")
        self.file_count_label.grid(row=6,column=0,sticky="nsew")
        self.canvas.grid(row=0,column=1,rowspan=36)
    
    def show_image(self, img):
        resized_img = img.resize((self.IMAGE_SIZE, self.IMAGE_SIZE))

        # Have to declare the image to display as a global, otherwise garbage collections
        # deletes it before it can be shown
        global temp
        temp = ImageTk.PhotoImage(resized_img)
        self.canvas.create_image(0,0,anchor=tk.NW,image=temp)
        self.canvas.update()
    
    def get_file(self, file_path):
        path = fd.askdirectory()
        print("Path: ",path)
        file_num = ct.get_file_count(self, path)
        file_path.insert(0, path+"/")
        print("File count: ", file_num)

root = tk.Tk()
window = Frame(root)
root.mainloop()