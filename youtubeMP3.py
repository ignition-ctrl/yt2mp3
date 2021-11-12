import re
import youtube_dl
import sys
import os
import getpass
import eyed3


def download_music(ytname=None, filename=None, heredeterminer=None):
    if ytname == None: 
        linkfinder = input("Please enter your link\n")
        if re.match("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?[\w\?=]*)?", linkfinder):
            ytname = str(linkfinder)
        else:
            print("No link found; please try again")
            exit(1)
    else:
        if re.match("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?[\w\?=]*)?", ytname):
            ytname = str(ytname)
            titlefinder = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s', 'quiet': 'True',})
            titlelist = titlefinder.extract_info(ytname, download=False)
            titlename = titlelist.get("title", None)
            print(titlename)
        else:
            newlinkfind = input("Not a valid link; please re-enter\n")
            ytname = str(newlinkfind)
    name = getpass.getuser() 
    if filename == None:
        namefinder = input("Please enter your desired filename for the .mp3 file\n")
        filename = str(namefinder)
        print("Continuing with " + str(filename) + " as filename")
    else:
        print("Continuing with " + str(filename) + " as filename")
    # if heredeterminer == None:
    #     herefinder = input("Do you want to download the file in the current directory?\n")
    #     heredeterminer = str(herefinder)
    heredeterminer = 'yes'
    filedir = os.getcwd() 
    defaultname = False
    if filename == "":
        defaultname = True
        print("Continuing with default filename")
    cwdpath = (str(filedir) + "/" + "%(title)s.%(ext)s") if defaultname == True else (str(filedir) + "/" + str(filename) + ".%(ext)s")
    defaultpath = ("/home/" + name + "/pythondir/yt2mp3/downloaded/" + "%(title)s.%(ext)s") if defaultname == True else ("/home/" + name + "/pythondir/yt2mp3/downloaded/" + str(filename) + "%.(ext)s")
    lengthfinder = youtube_dl.YoutubeDL({'quiet': True, 'forceduration': True})
    infolist = lengthfinder.extract_info(ytname, download=False)
    vidlengthsec = infolist.get('duration', None)
    vidlengthmin = (vidlengthsec / 60)
    if vidlengthmin > 10:
        print("Video length is " + str(vidlengthmin) +"\n Downloading as .m4a for best audio")
        m4aformat = True
    else:
        m4aformat = False
    params = {
            'writethumbnail': True,
            'format': 'bestaudio/best' if m4aformat == False else 'm4a',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 
                'preferredquality': '192',},
                {'key': 'EmbedThumbnail'},] if m4aformat == False else [],
            'cookiefile' : '~/codedir/pythondir/yt2mp3/youtube.com_cookies.txt',
            'source_address':'0.0.0.0',
            'outtmpl':  (cwdpath) if heredeterminer == "yes" or "Yes" or "y" else (defaultpath)
}
    youtube = youtube_dl.YoutubeDL(params) #the bulk of the work is made by youtube-dl.
    youtube.download([ytname])
    print("Downloading in current directory...")
    if m4aformat == True:
        print("Skipping eyeD3 tagging, assuming file is a mix")
    else:
        try:
            audioname = (filename+".mp3") if heredeterminer == "yes" or "Yes" or "y" else ("/home/" + name + "/pythondir/yt2mp3/downloaded/" + filename+".mp3")
            audiofile = eyed3.load(str(audioname))
            print(audioname+" loaded\nEyeD3 tagging:")
        except:
            audioname = (titlename+".mp3") if heredeterminer == "yes" or "Yes" or "y" else ("/home/" + name + "/pythondir/yt2mp3/downloaded/"+titlename+".mp3")
            audiofile = eyed3.load(str(audioname))
            print(audioname+" loaded\nEyeD3 tagging:")
        artistfinder = input("Who is the artist?\n")#always remember your '\n's!
        audiofile.tag.artist = str(artistfinder)
        trackfinder = input("Track name?\n")
        audiofile.tag.title = str(trackfinder)
        audiofile.tag.save()
        print("Music downloaded")


if __name__ == '__main__':
    try:
        download_music(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        try:
            download_music(sys.argv[1], sys.argv[2])
        except:
            if len(sys.argv) == 2:
                download_music(sys.argv[1])
            else:
                print('No arguments')
                download_music()
