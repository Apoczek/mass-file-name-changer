#Program which rename every file in directory according to pattern:
#<new_name>[i].ext
#new_name - core of the new name
#[i] - another number
#.ext - given type of file


import os
import tkinter as tk
from tkinter import filedialog


class Application(tk.Frame): #TODO add event handling for "enter" and "escape"
                             #TODO add status bar to show all the files name before and after renaming, print "finished" at the end
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()
        #self.tempdir = os.getcwd()
        self.create_widgets()

    def renaming(self): #TODO handle situation where no files with given type
                        #TODO popup window if any special char is given to file_type entry
                        #TODO handle forbidden chars in name entry
                        #TODO handle blank entries
                        #TODO limit entries chars number
        directory = self.tempdir.get()
        new_name = self.new_name.get()
        file_type = '.' + self.file_type.get()
        i = 1
        for file in os.listdir(directory):
            if file.endswith(file_type):
                os.rename(file, new_name + str(i) + file_type)
                print(file + ' --> ' + new_name + str(i) + file_type)
                i += 1

    def given_dir(self):
        self.tempdir.set(filedialog.askdirectory(parent=root,
                                                 initialdir=self.tempdir.get(),
                                                 title='Please select a directory'))

    def create_widgets(self):

        l1 = tk.Label(self.main_frame, text='Katalog docelowy: ')
        l1.grid(row=0, column=0, columnspan=2)

        self.tempdir = tk.StringVar()
        self.tempdir.set(os.getcwd())
        l2 = tk.Label(self.main_frame, textvariable=self.tempdir)
        l2.grid(row=1, column=0, columnspan=2)

        b1 = tk.Button(self.main_frame, text='Change directory', command=self.given_dir)
        b1.grid(row=2, column=0, columnspan=2)

        l3 = tk.Label(self.main_frame, text='Insert new name for files: ')
        l3.grid(row=3, column=0, columnspan=2)

        self.new_name = tk.StringVar()
        e1 = tk.Entry(self.main_frame, textvariable=self.new_name)
        e1.grid(row=4, column=0, columnspan=2)

        l4 = tk.Label(self.main_frame, text='Insert file type (example: txt): ')
        l4.grid(row=5, column=0, columnspan=2)

        self.file_type = tk.StringVar()
        e2 = tk.Entry(self.main_frame, textvariable=self.file_type)
        e2.grid(row=6, column=0, columnspan=2)

        b2 = tk.Button(self.main_frame, text='Rename', width=12, command=self.renaming)
        b2.grid(row=7, column=0, padx=5, pady=5)

        b3 = tk.Button(self.main_frame, text='Close', width=12, command=root.destroy)
        b3.grid(row=7, column=1, padx=5, pady=5)


root = tk.Tk()
root.resizable(0, 0)
root.title('Mass name changer')
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 300
h = 200
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
app = Application(root)
root.mainloop()
