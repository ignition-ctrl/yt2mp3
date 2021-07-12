import re
import youtube_dl
import sys
import os
import getpass
sys.path.insert(1, '~/pythondir/yt2mp3/thumbnails')
from downloadimg import download_thumbnail
import eyed3


def download_music(ytname=None, filename=None, heredeterminer=None):
    
    if ytname == None: 
        linkfinder = input("Please enter your link\n")
        if re.match("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?", linkfinder):
            ytname = str(linkfinder)
        else:
            print("No link found; please try again")
            exit(1)
    name = getpass.getuser() 
    if filename == None:
        namefinder = input("Please enter your desired filename for the .mp3 file\n")
        filename = str(namefinder)
    if heredeterminer == None:
        herefinder = input("Do you want to download the file in the current directory?\n")
        heredeterminer = str(herefinder)
    filedir = os.getcwd() 
    defaultname = False
    if filename == "":
        defaultname = True
    cwdpath = (str(filedir) + "/" + "%(title)s.%(ext)s") if defaultname == True else (str(filedir) + "/" + str(filename) + ".%(ext)s")
    defaultpath = ("/home/" + name + "/pythondir/yt2mp3/downloaded/" + "%(title)s.%(ext)s") if defaultname == True else ("/home/" + name + "/pythondir/yt2mp3/downloaded/" + str(filename) + "%.(ext)s")
    params = {
            'writethumbnail': True,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 
                'preferredquality': '192',},
                {'key': 'EmbedThumbnail'},],
            'cookiefile' : '~/pythondir/yt2mp3/youtube.com_cookies.txt',
            'source_address':'0.0.0.0',
            'outtmpl':  (cwdpath) if heredeterminer == "yes" or "Yes" or "y" else (defaultpath)
}
    youtube = youtube_dl.YoutubeDL(params) #the bulk of the work is made by youtube-dl.
    ytname = str(ytname)
    youtube.download([ytname])
    titlefinder = youtube_dl.YoutubeDL({'outtmpl': '%(title)s'})
    titlelist = titlefinder.extract_info(ytname, download=False)
    titlename = titlelist.get("title", None)
    try:
        audioname = (filename+".mp3") if heredeterminer == "yes" or "Yes" or "y" else ("/home/" + name + "/pythondir/yt2mp3/downloaded/" + filename+".mp3")
        audiofile = eyed3.load(audioname)
    except:
        audioname = (titlename+".mp3") if heredeterminer == "yes" or "Yes" or "y" else ("/home/" + name + "/pythondir/yt2mp3/downloaded/"+titlename+".mp3")
        audiofile = eyed3.load(audioname)
    #here, I'm adding eyed3 tagging, as the inbuilt youtube-dl tagging can be unreliable. It uses try except to find the right file using the yt title or the filename. 
    artistfinder = input("Who is the artist?\n")#always remember your '\n's!
    audiofile.tag.artist = str(artistfinder)
    albumfinder = input("Album?\n")
    audiofile.tag.album = str(albumfinder)
    trackfinder = input("Track name?\n")
    audiofile.tag.title = str(trackfinder)
    audiofile.tag.save()
    print("The thumbnail has been downloaded and embedded within the file. However, you can still download it seperately.")
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

    if len(sys.argv) >= 2:
        try:
            download_music(sys.argv[1], sys.argv[2], sys.argv[3])
        except:
            try:
                download_music(sys.argv[1], sys.argv[2])
            except:
                download_music(sys.argv[1])
    else:
        download_music()