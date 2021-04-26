import youtube_dl
import sys
import getpass

name = getpass.getuser()
arguments = sys.argv[1:]
filename = arguments[1]
arguments.pop()
ytname = arguments[0:]

params = {
        'format': 'bestaudio/best',        
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': "/home/" + name + "/pythondir/yt2mp3/" + str(filename) + ".mp3"
        }

youtube = youtube_dl.YoutubeDL(params)

youtube.download(ytname)

