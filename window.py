from tkinter import *
from youtube_functions import *

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