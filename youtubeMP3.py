import re
import youtube_dl
import sys
import os
import getpass
sys.path.insert(1, '~/pythondir/yt2mp3/thumbnails')
from downloadimg import download_thumbnail

"""
I am such a genius. I love this. Future Zack, (who hopefully got a job as a Linux SysAdmin, and is living the dream), this is how the
code works. I started with the basic formula, creating a function with a params dictionary to send to youtube-dl to download an mp3.
However, I started customizing it. I didn't want to have long filenames with the video id. (Though I later found out there was an outtmpl
option to remove the video id,) I made some changes to the argv passing so I could add a filename argument after the link. I was so proud.
I think I even edited the source code of youtube-dl to remove an annoying outtmpl error. Eventually, I added little things, like adding
a bash function to call the script anywhere, the option to download in the current directory, and even made a secondary program to 
download thumbnails. Also finding the user's name to accurately put songs in the downloaded folder (though I could have just used ~; 
story of my life). All of this, to culminate in the complete shipping of Zack's youtubeMP3 1.0. Here's how it works.
"""

def download_music(ytname=None, filename=None, heredeterminer=None):
    #print("entry")
    #So, right off the bat, this function takes three arguments, but optionally! I set each argument as None, and added
    #behavior to interactively supply any missing parts. Genius, I know
    if ytname == None: #so, here it is. If ytname is None, interactively have the user put a link in, and if it's not valid exit out.
        linkfinder = input("Please enter your link\n")
        if re.match("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?", linkfinder):
            #download_music(str(linkfinder), filename, heredeterminer) #This sends the user through the function again, with linkfinder taking ytname
            """
            actually, these comments are wrong. After I finished writing them, I realized instead of creating more iterations, I can just
            reassign the variable to the input. That way, it's faster and only runs once. I can be such an idiot. Also, fixed some sys.argv
            errors. It works perfectly now. 1.0 is ready.
            """
            ytname = str(linkfinder)
            #since linkfinder is not None, it won't trigger this code again.
            #print("exit")
            #exit(0) #However, once download_music finished, it will continue at the first iteration. The exit guarantees there's no loop
        else:
            print("No link found; please try again")
            exit(1)
    #else:
    #hacker typing idk
    #    print("ytname different from None")
    name = getpass.getuser() #just a way to get the name so that it can be put in the full outtmpl path. I guess I can just use ~, though
    if filename == None:
        namefinder = input("Please enter your desired filename for the .mp3 file\n")
        #download_music(ytname, str(namefinder), heredeterminer)
        filename = str(namefinder)
        #print("exit")
        #exit(0) # same sort of None verifying. It's really genius, whoever put this in python
    #else:
        #print("filename different")
    if heredeterminer == None:
        herefinder = input("Do you want to download the file in the current directory?\n")
        #download_music(ytname, filename, str(herefinder)) #Now, at this point, this should be the final iteration of the function, since all arguments are supplied
        heredeterminer = str(herefinder)
        #print("exit")
        #exit(0) #should be the final exit out of the iterations
    filedir = os.getcwd() #just incase they want to download in the current directory
    params = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 
                'preferredquality': '192',
                }],
            'cookiefile' : '~/pythondir/yt2mp3/youtube.com_cookies.txt',
            'source_address':'0.0.0.0',
            'outtmpl':  (str(filedir) + "/" + str(filename) + ".") if heredeterminer == "yes" or "Yes" or "y" else ("/home/" + name + "/pythondir/yt2mp3/downloaded/" + str(filename) + ".")
            #above is a really long line, with ternary operators. Useful for changing outtmpl's definition
}
    youtube = youtube_dl.YoutubeDL(params) #the bulk of the work is made by youtube-dl. Geniuses, they are
    ytname = str(ytname)
    youtube.download([ytname])
    determiner = input("Do you want to download the thumbnail?\n") #a little interactive determiner to download the thumbnail
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
        #here, if I'm running the script directly, it tries running it with command line arguments
        #Of course, if they are no arguments it throws an IndexError. So it moves on 
        #here, now it just calls it without any sys.argv. everything is set to None, and the iterations go to work.

#That's it! It should all be good now, so enjoy working on whatever projects you're on now!
