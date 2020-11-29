import pytube
import os

def downloading(url):
    video = pytube.YouTube(url)
    for stream in video.streams:
        if "video" in str(stream) and "mp4" in str(stream) and "720p" in str(stream):
            get_itag = str(stream)
            hd_itag = get_itag[15:18].replace('"', '')
            break
    stream = video.streams.get_by_itag(hd_itag)
    print(f"Downloading {video.title}...")
    stream.download()
    print("Done. Your video was downloaded.")
    os.system('cls')
