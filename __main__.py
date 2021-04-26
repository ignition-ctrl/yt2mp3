#!/usr/bin/env python
# -*- coding: utf-8 -*-

import youtube_dl
import sys
import getpass


def main():
    name = getpass.getuser()
    arguments = sys.argv[1:]
    filename = arguments[1]
    arguments.pop()
    ytname = arguments[0:]
    params = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': "/home/" + name + "/pythondir/yt2mp3/downloaded/" + str(filename) + "."
    }
    youtube = youtube_dl.YoutubeDL(params)

    youtube.download(ytname)
    # Code goes over here.
    return 0


if __name__ == "__main__":
    main()