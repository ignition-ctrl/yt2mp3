import subprocess
import sys
import youtube_dl
import os


def download_thumbnail(link, chosenname=None, determiner=None):
    if chosenname == None:
        namefinder = input("Please enter your desired filename\n")
        chosenname = str(namefinder)
    if determiner == None:
        detfinder = input("Do you want to download it in the current directory?\n")
        determiner = detfinder
    if determiner == "yes":
        outdir = (str(os.getcwd()) + "/")
    else:
        print("Keyword 'yes' not found; continuing download at ~/pythondir/yt2mp3/thumbnails")
        outdir = "~/pythondir/yt2mp3/thumbnails/"
    #youtubedl_out = subprocess.run(['youtube-dl', '--write-thumbnail', '--force-ipv4', '-o', (outdir + chosenname), '--skip-download', link])
    params = {
        "cookiefile" : "~/pythondir/yt2mp3/youtube.com_cookies.txt",
        "skip_download" : True,
        "source_address" : "0.0.0.0",
        "outtmpl" : (outdir + chosenname + "."),
        "writethumbnail" : True,
    }
    youtube = youtube_dl.YoutubeDL(params)
    youtube.download([link])
    print("Download Successful; Now Converting")
    pngname = (str(outdir) + str(chosenname) + ".png")
    try:
        subprocess.run(['dwebp', (outdir+chosenname+".webp"), '-o', pngname])
    except:
        subprocess.run(['dwebp', (outdir+chosenname+".jpg"), '-o', pngname])
    subprocess.run(['convert', pngname, (chosenname + ".jpg")])
    if os.path.exists(pngname):
        os.remove(pngname)
    if os.path.exists(chosenname+".webp"):
        os.remove(chosenname+".webp")


if __name__ == "__main__":
    try:
        download_thumbnail(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        download_thumbnail(sys.argv[1])
    # try:
    #     if (len(sys.argv) < 3):
    #         download_thumbnail(sys.argv[1], sys.argv[2], 'no')
    #     elif (len(sys.argv) == 3):
    #         download_thumbnail(sys.argv[1], sys.argv[2], sys.argv[3])

    # except IndexError:
    #     raise NameError("Please provide a link and your desired filename")

# cleaned up the code! call this function from main with sys.arv being the arguments
