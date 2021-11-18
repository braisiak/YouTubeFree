from tkinter import *
from tkinter import font
from moviepy.editor import *
import pytube
import os

# Creating window
app = Tk()
app.geometry("390x135")
app.title("YouTubeFree")
app.resizable(0, 0)
app.iconbitmap('icon.ico')

# Changing variables
quality = StringVar()
format = StringVar()

# Downloading .mp3 files
def downloading_mp3():
    song = pytube.YouTube(LinkEntry.get())
    for stream in song.streams:
        if "audio" in str(stream) and "mp4" in str(stream):
            get_itag = str(stream)
            hd_itag = get_itag[15:18].replace('"', '')
            break
    stream = song.streams.get_by_itag(hd_itag)
    song_title = ((((((((((song.title).replace(" ", "")).replace(".", "")).replace("/", "")).replace("|", "")).replace("<", "")).replace(">", "")).replace("*", "")).replace(":", "")).replace("?", "")).replace('"', '')
    stream.download(filename=f"{song_title}.mp4")
    mp4_file = fr'{song_title}.mp4'
    mp3_file = fr'{song_title}.mp3'
    audioclip = AudioFileClip(mp4_file)
    audioclip.write_audiofile(mp3_file, verbose=False, logger=None)
    audioclip.close()
    os.system(f'del {song_title}.mp4')
    os.system(f'rename {song_title}.mp3 "{song.title}.mp3"')    

# Downloading .mp4 files
def downloading_mp4():
    global quality
    video = pytube.YouTube(LinkEntry.get())
    for stream in video.streams:
        if "video" in str(stream) and "mp4" in str(stream) and str(quality.get()) in str(stream):
            get_itag = str(stream)
            hd_itag = get_itag[15:18].replace('"', '')
            break
    stream = video.streams.get_by_itag(hd_itag)
    stream.download()

# Activate video quality checkboxes when format is set to .mp4
def activateCheckboxes():
    SDCheckBox['state'] = 'normal'
    HDCheckBox['state'] = 'normal'
    FHDCheckBox['state'] = 'normal'

# Deactivate video quality checkboxes when format is set to .mp3
def deactivateCheckboxes():
    SDCheckBox['state'] = 'disabled'
    HDCheckBox['state'] = 'disabled'
    FHDCheckBox['state'] = 'disabled'

# Check chosen format and download the file
def download():
    global format
    if format.get() == "mp3":
        downloading_mp3()
    elif format.get() == "mp4":
        downloading_mp4()
    else:
        return

# GUI widgets
downloading = Frame(app)
downloading.grid()

SpaceLabel = Label(downloading, text="")
SpaceLabel.grid(row=0, column=0)

LinkLabel = Label(downloading, text="Paste video link:", font="Bahnschrift 10")
LinkLabel.grid(row=1, column=1, columnspan=3)

LinkEntry = Entry(downloading, width=45)
LinkEntry.grid(row=2, column=1, columnspan=3)

DownloadButton = Button(downloading, text="Download", command=download, font="Bahnschrift 10")
DownloadButton.grid(row=3, column=2)

Mp3RadioButton = Radiobutton(downloading, text=".mp3", variable=format, value="mp3", command=deactivateCheckboxes,font="Bahnschrift 10")
Mp3RadioButton.grid(row=4, column=1,)
Mp3RadioButton.select()

Mp4RadioButton = Radiobutton(downloading, text=".mp4", variable=format, value="mp4", command=activateCheckboxes,font="Bahnschrift 10")
Mp4RadioButton.grid(row=4, column=3)

ColumnBreak = Label(downloading, text="‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎")
ColumnBreak.grid(row=1, column=4)

QualityLabel = Label(downloading, text="Video quality:", font="Bahnschrift 10")
QualityLabel.grid(row=0, column=5)

SDCheckBox = Radiobutton(downloading, text="480p", variable=quality, value="480p", font="Bahnschrift 10", state=DISABLED)
SDCheckBox.grid(row=1, column=5)

HDCheckBox = Radiobutton(downloading, text="720p", variable=quality, value="720p", font="Bahnschrift 10", state=DISABLED)
HDCheckBox.grid(row=2, column=5)
HDCheckBox.select()

FHDCheckBox = Radiobutton(downloading, text="1080p", variable=quality, value="1080p", font="Bahnschrift 10", state=DISABLED)
FHDCheckBox.grid(row=3, column=5)

app.mainloop()