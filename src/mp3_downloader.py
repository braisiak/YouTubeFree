import pytube
import os

def downloading(url):
    song = pytube.YouTube(url)
    for stream in song.streams:
        if "audio" in str(stream) and "mp4" in str(stream):
            get_itag = str(stream)
            hd_itag = get_itag[15:18].replace('"', '')
            break
    stream = song.streams.get_by_itag(hd_itag)
    song_title = ((song.title).replace(" ", "")).replace(".", "")
    print(f"Downloading {song.title}...")
    stream.download(filename=song_title)
    print("Done. Your song was downloaded.")
    print("Converting...")
    os.system(f'ffmpeg -i {song_title}.mp4 {song_title}.mp3')
    os.system(f'del {song_title}.mp4')
    print("Successfully converted.")
    os.system(f'rename {song_title}.mp3 "{song.title}.mp3"')
    print("File renamed.")
    os.system('cls')
        
