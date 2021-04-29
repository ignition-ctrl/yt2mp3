import subprocess
import sys
import re
import os

def download_thumbnail(link, chosenname):
    youtubedl_out = subprocess.check_output(['youtube-dl', '--write-thumbnail', '--force-ipv4', '-o', chosenname, '--skip-download', link])
    print(str(youtubedl_out))
    pngname = str(str(chosenname) + ".png")
    subprocess.run(['dwebp', (chosenname+".webp"), '-o', pngname])
    subprocess.run(['convert', pngname, (chosenname + ".jpg")])
    if os.path.exists(pngname):
          os.remove(pngname)
    else:
        print("The png file does not exist")
    if os.path.exists(chosenname+".webp"):
        os.remove(chosenname+".webp")
    else:
        print("the file does not exist")

download_thumbnail(sys.argv[1], sys.argv[2])
#cleaned up the code! call this function from main with sys.arv being the arguments