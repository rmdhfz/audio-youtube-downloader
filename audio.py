
import tkinter as tk
import youtube_dl as yd
from tkinter import *
from tkinter import messagebox, filedialog

def CreateWidgets():

    linkLabel = Label(root, text="Link : ", bg="slategrey")
    linkLabel.config(anchor=CENTER)
    linkLabel.grid(row=1, column=0, pady=5, padx=5)
    root.linkText = Entry(root, width=40)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)
    destinationLabel = Label(root, text="Dir : ", bg="slategrey")
    destinationLabel.config(anchor=CENTER)
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)
    root.destinationText = Entry(root, width=25)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)
    browseButton = Button(root, text="Browse", command=Browse, width=10)
    browseButton.grid(row=2, column=2, pady=5, padx=5)
    dwldButton = Button(root, text="Download", command=Download, width=20)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)

def Browse():
    root.destinationDIR = filedialog.askdirectory(initialdir="/root/Documents/youtube/audio")
    root.destinationText.insert('1', root.destinationDIR)

def Download():
    videoLink = root.linkText.get()
    savePath = root.destinationText.get()
    audioDownloadOptions = {
        'format':'bestaudio/best',
        'outtmpl': savePath+"/%(title)s.%(ext)s",
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }],
    }


    with yd.YoutubeDL(audioDownloadOptions) as aud_dwld:
        aud_dwld.download([videoLink])

    messagebox.showinfo("Success", "Video converted and downlaoded as audio!")

root = tk.Tk()
root.geometry("450x120")
root.title("Youtube Audio Downloader")
root.resizable(False, False)
root.config(background="slategrey")
CreateWidgets()
root.mainloop()