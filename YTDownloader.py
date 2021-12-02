# This algorithm downloads a certain video from YouTube,
# After it converts the video file to a mp3 format

# It is necesary to install the pytube and moviepy modules
# That can be done using the pip install pytube and moviepy commands

# moviepy documentation: https://zulko.github.io/moviepy/
# pytube documentation: https://pytube.io/en/latest/

import pytube
import moviepy.editor as mp
from pytube import YouTube

url = "https://www.youtube.com/watch?v=OBoZHbJKHXc"
path = "./"

yt = pytube.YouTube(url)
yt.streams.first().download(path)

name = ("./3 Doors Down- Landing in London lyrics.3gpp")
clip = mp.VideoFileClip(name)

clip.audio.write_audiofile("3 Doors Down - Landing in London.mp3")