import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer

class Player(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.playlist = []

        self.create_frames()
        self.track_widgets()
        self.control_widgets()
        self.tracklist_widgets()

    def create_frames(self):
        self.track = tk.LabelFrame(self, text='Song Track',
                                   font=("times new roman",15,"bold"),
                                   bg="grey",fg="white",bd=5,relief=tk.GROOVE)
        self.track.configure(width=410,height=300)
        self.track.grid(row=0, column=0, padx=10)

        self.tracklist = tk.LabelFrame(self, text=f'PlayList - {str(len(self.playlist))}',
                                   font=("times new roman",15,"bold"),
                                   bg="grey",fg="white",bd=5,relief=tk.GROOVE)
        self.tracklist.config(width=190,height=400)
        self.tracklist.grid(row=0, column=1, rowspan=3, pady=5)

        self.controls = tk.LabelFrame(self,
                                   font=("times new roman",15,"bold"),
                                   bg="white",fg="white",bd=2,relief=tk.GROOVE)
        self.controls.config(width=410,height=80)
        self.controls.grid(row=2, column=0, pady=5, padx=10)

    def track_widgets(self):
        self.canvas = tk.Label()

    def control_widgets(self):
        pass

    def tracklist_widgets(self):
        pass

root = tk.Tk()
root.geometry('600x400')
root.wm_title('Musicxy MP3 Player')

img = PhotoImage(file = 'images/music.gif')
next_ = PhotoImage(file = 'images/next.gif')
prev = PhotoImage(file = 'images/previous.gif')
play = PhotoImage(file = 'images/play.gif')
pause = PhotoImage(file = 'images/pause.gif')

app = Player(master=root)
app.mainloop()
