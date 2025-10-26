from pytubefix import YouTube
from pytubefix.cli import on_progress

print("\nYouTube Vidéo Downloader\n")

url = input("\nEnter YouTube video URL: ")

print("\nConnecting to YouTube...\n")

yt = YouTube(url, on_progress_callback = on_progress)

print(f"Title: {yt.title}")
print(f"Author: {yt.author}")
print(f"Views : {yt.views}")

stream = yt.streams.get_highest_resolution()

print("\nDownloading...\n")

stream.download() 

print("\nDownload completed!\n")

print(f"\nVideo saved to: {stream.default_filename}\n\n")