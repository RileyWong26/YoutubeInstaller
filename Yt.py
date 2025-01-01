from pytubefix import YouTube
import os
path = os.getcwd() + "\YoutubeInstaller\Videos"
print(path)
def download(link):
    video = YouTube(link)
    print(video.check_availability())
    try:
        bestVideo = video.streams.get_highest_resolution()
    except:
        print('error')
    try:
        videodownload = bestVideo.download(output_path=path)
        print('SUCCESS')
        filetype(videodownload)
    except:
        print("An error occurred")

def filetype(videodownload):
    file = input("What file type (mp4/mp3): ")
    if file.strip().lower() == "mp3":
        type = '.mp3'
    else:
        type = '.mp4'

    base, end = os.path.splitext(videodownload)
    newfile = base + type
    os.rename(videodownload, newfile)

link = ""
while link.strip().lower() !="exit":
    link = input("Link(exit to quit): ")
    video = YouTube(link)
    print(video.title)

    confirm = input("This video?(y/n): ")
    while confirm.strip().lower() != 'y':
        link = input("Link: ")
        video = YouTube(link)
        print(video.title)
        confirm = input("This video?(y/n): ")

    download(link)