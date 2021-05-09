import subprocess
import sys
import re
import os

def download_thumbnail(link, chosenname, determiner, current):
    if determiner == "yes":
        outdir = current + "/"
    else:
        outdir = "~/pythondir/yt2mp3/thumbnails/"
    youtubedl_out = subprocess.check_output(['youtube-dl', '--write-thumbnail', '--force-ipv4', '-o', (outdir+ chosenname), '--skip-download', link])
    pngname = (str(outdir) + str(chosenname) + ".png")
    subprocess.run(['dwebp', (outdir+chosenname+".webp"), '-o', pngname])
    subprocess.run(['convert', pngname, (chosenname + ".jpg")])
    if os.path.exists(pngname):
          os.remove(pngname)
    if os.path.exists(chosenname+".webp"):
        os.remove(chosenname+".webp")

if __name__ == "__main__":
    try:
        download_thumbnail(sys.argv[1], sys.argv[2])
    except IndexError:
        raise NameError("Please provide a link and your desired filename")
#cleaned up the code! call this function from main with sys.arv being the arguments
