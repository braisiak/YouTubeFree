from src import mp3_downloader
from src import mp4_downloader

def main():
    global url
    file_format = input("mp3 or mp4: ") # Ask user about file format
    url = input("Paste video url: ") # Ask user for url
    if file_format == "mp3":
        mp3_downloader.downloading(url)
        main()
    elif file_format == "mp4":
        mp4_downloader.downloading(url)
        main()
    else:
        print("Invalid value. Try again.")
        main()

main()
