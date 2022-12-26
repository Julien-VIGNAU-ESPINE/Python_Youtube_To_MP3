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
    """Button Placeholder"""
    print(txt.get())

def download():
    """Search and dowload the video on MP3 format"""
    download_from_search(txt.get())

# Window configuration
window = Tk()
window.title("YouTube To MP3")
window.geometry('800x500')
window.configure(bg="#333")

# Title configuration
title = Label(window, text="YouTube to MP3", font=("Arial Bold", 50), bg="#333",
fg="#F00")
title.grid(column=0, row=0)

# Text input configuration
title = Label(window, text="Music title to download", font=("Arial Bold", 15),
bg="#333", fg="#FFF")
title.grid(column=0, row=5)
txt = Entry(window,width=40)
txt.grid(column=0, row=6)

# Button configuration
btn = Button(window, text="Download", command=download)
btn.grid(column=0, row=10)

# Run the window
window.mainloop()