#!/usr/bin/env python
# -*- coding: utf-8 -*-

import youtube_dl
import sys
import getpass
import youtubeMP3
    
    #if len(sys.argv) < 3:
    #    if len(sys.argv) == 2:
    #        print("Please provide a filename without .mp3\nABORTING")
    #        exit(1)
    #    elif len(sys.argv) == 1:
    #        print("Please provide a Youtube link and a filename without .mp3\nABORTING")
    #        exit(1)
    #    else:
    #        print("Please provide only a YT link and a filename (without .mp3) separated by a single space.")
    #name = getpass.getuser()
    #arguments = sys.argv[1:]
    #filename = arguments[1]
    #arguments.pop()
    #ytname = arguments[0:]
    #params = {
    #    'format': 'bestaudio/best',
    #    'postprocessors': [{
    #        'key': 'FFmpegExtractAudio',
    #        'preferredcodec': 'mp3',
    #        'preferredquality': '192',
    #    }],
    #    'outtmpl': "/home/" + name + "/pythondir/yt2mp3/downloaded/" + str(filename) + "."
    #}
    #youtube = youtube_dl.YoutubeDL(params)

    ##youtube.download(ytname)
    # Code goes over here.
    #return 0


if __name__ == "__main__":
    youtubeMP3.download_music(str(sys.argv[1]), str(sys.argv[2]))
