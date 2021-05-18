import youtube_dl
import sys
import os
import getpass
sys.path.insert(1, '~/pythondir/yt2mp3/thumbnails')
from downloadimg import download_thumbnail

if len(sys.argv) < 3:
    print("File will be downloaded in ~/pythondir/yt2mp3/downloaded")
    if len(sys.argv) == 2:
        print("Please provide a filename without .mp3\nABORTING")
        exit(1)
    elif len(sys.argv) == 1:
        print("Please provide a Youtube link and a filename without .mp3\nABORTING")
        exit(1)
    else:
        print("Please provide only a YT link and a filename (without .mp3) separated by a single space.")

def download_music(ytname, filename, location):
    name = getpass.getuser()
    if str(location) == "here":
        filedir = os.getcwd()
        params = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'source_address':'0.0.0.0',
            'outtmpl': str(filedir) + "/" + str(filename) + "."
}
    else:
        params = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3', 
                    'preferredquality': '192',
                    }],
                'source_address':'0.0.0.0',
                'outtmpl': "/home/" + name + "/pythondir/yt2mp3/downloaded/" + str(filename) + "."
}
    youtube = youtube_dl.YoutubeDL(params)
    youtube.download([ytname])
    determiner = input("Do you want to download the thumbnail?\n")
    if (determiner == "yes"):
        seconddeter = input("Do you want to download it in the current directory?\n")
        if seconddeter == "yes":
            download_thumbnail(str(ytname), str(filename), "yes")
        else:
            download_thumbnail(str(ytname), str(filename), "no")
    elif (determiner == 'no' or "No" or "n"):
        exit(0)
    else:
        exit(1)
if __name__ == '__main__':
    if len(sys.argv) == 3:
        download_music(sys.argv[1], sys.argv[2], '')
    else:
        download_music(sys.argv[1], sys.argv[2], sys.argv[3])
