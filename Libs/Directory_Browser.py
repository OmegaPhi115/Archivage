from tkinter import filedialog
from tkinter import *

class run():
    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        self.folder_path
        self.filename = filedialog.askdirectory()
        self.folder_path.set(filename)

    def __init__(self):
        self.folder_path = StringVar()

        self.lbl1 = Label(textvariable=self.folder_path, bg="#c6c6c6")
        self.lbl1.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

        self.button2 = Button(text="Browse", command=self.browse_button)
        self.button2.grid(row=1, column=0, pady=5, padx=10)

        self.button2 = Button(text="Done", command=self.destroy)
        self.button2.grid(row=1, column=1, pady=5, padx=10)

        mainloop()