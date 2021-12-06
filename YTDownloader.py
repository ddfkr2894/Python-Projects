# This algorithm downloads a certain video from YouTube,
# After it converts the video file to a mp3 format

# It is necesary to install the pytube and moviepy modules
# That can be done using the pip install pytube and moviepy commands

# moviepy documentation: https://zulko.github.io/moviepy/
# pytube documentation: https://pytube.io/en/latest/

#import pytube
#import moviepy.editor as mp
#from pytube import YouTube
#
#url = "https://www.youtube.com/watch?v=OBoZHbJKHXc"
#path = "./"
#
#yt = pytube.YouTube(url)
#yt.streams.first().download(path)
#
#name = ("./GeneratedFiles/3 Doors Down- Landing in London lyrics.3gpp")
#clip = mp.VideoFileClip(name)
#
#clip.audio.write_audiofile("3 Doors Down - Landing in London.mp3")

from contextlib import redirect_stderr
import tkinter
from tkinter import *
import pytube
import moviepy.editor as mp
from pytube import YouTube

def getmp3():
    url = urlTextBox.get()
    path = "./GeneratedFiles"

    try:
        yt = pytube.YouTube(url)
        yt.streams.first().download(path)

        name = ("./GeneratedFiles/" + yt.title + ".3gpp")
        clip = mp.VideoFileClip(name)

        clip.audio.write_audiofile(yt.title + ".mp3")
        outputMessage['text'] = "The mp3\n{}\nwas downloaded successfully :D".format(yt.title)
    except:
        outputMessage['text'] = "Something went wrong trying to download\n{}\n:(".format(yt.title)
    finally:
        urlTextBox.delete(0, END)

WindowApp = Tk()
WindowApp.title("mp3 YouTube Downloader")
WindowApp.geometry("300x300")

labelTitle = Label(WindowApp, text = "Youtube Downloader")
labelTitle.pack()

labelInstructions = Label(WindowApp, text = "¡Welcome!, \njust paste the URL video and \nyou'll get that mp3 :)")
labelInstructions.pack()

urlTextBox = Entry(WindowApp)
urlTextBox.pack()

getMp3Button = Button(WindowApp, text = "Get mp3!", command = getmp3)
getMp3Button.pack()

outputMessage = Label(text = "", fg = "red")
outputMessage.pack()

WindowApp.mainloop()