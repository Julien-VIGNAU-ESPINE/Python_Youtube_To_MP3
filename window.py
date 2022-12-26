# YOUTUBE_TO_MP3
# Window
# Author : Julien VIGNAU-ESPINE
# 26/12/2022 23:28

# =============================================================================
# README
# =============================================================================

# =============================================================================
# IMPORTATIONS
# =============================================================================

from tkinter import *
from youtube_functions import *

# =============================================================================
# CODE
# =============================================================================

def clicked():
    print(txt.get())

def download():
    download_from_search(txt.get())

window = Tk()
window.title("Youtube To MP3")
window.geometry('500x300')
txt = Entry(window,width=10)
txt.grid(column=0, row=0)
btn = Button(window, text="Click Me", command=download)
btn.grid(column=2, row=0)

window.mainloop()