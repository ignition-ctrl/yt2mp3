import subprocess
import sys
import re
import os

if len(sys.argv) < 2:
    print("No Youtube link providedi and/or filename\nABORTING")
    exit(1)
link = str(sys.argv[1])
chosenname = str(sys.argv[2])
#youtubedl_out = subprocess.call(['youtube-dl --list-thumbnails --verbose --force-ipv4 kW3cIU2B_AA'], shell=True, stdout=subprocess.PIPE)
youtubedl_out = subprocess.check_output(['youtube-dl', '--list-thumbnails', '--force-ipv4', link])
print(str(youtubedl_out))
#for line in str(youtubedl_out):
#    if "maxresdefault" not in str(line):
#        print("No match")
#        continue
#    else:
#        print("Match")
#        imgurl = str(line)
#imgurl = re.search("/maxresdefault/g", str(youtubedl_out)).group(0)
newytoutput = youtubedl_out.decode("utf-8")
imgurl =re.search("(?P<url>https?://[^\s]+)", newytoutput).group('url')
print(str(imgurl))
pngname = str(str(chosenname) + ".png")
determiner = input("is jpg or webp?\n")
if determiner == "jpg":
    ending = ".jpg"
elif determiner == "webp":
    ending = ".webp"
wgetout = subprocess.check_output(['wget', "-O", (chosenname+ending), imgurl])
print(wgetout)
cont = input("Continue with conversion to jpg? only if file is webp\n")
if cont == "yes":
    subprocess.run(['dwebp', (chosenname+".webp"), '-o', pngname])
    subprocess.run(['convert', pngname, (chosenname + ".jpg")])
    if os.path.exists(pngname):
          os.remove(pngname)
    else:
        print("The png file does not exist")
    if os.path.exists(chosenname+ending):
        os.remove(chosenname+ending)
    else:
        print("the file does not exist")
else:
    exit(0)


#wgetoutput = wgetout.decode("utf-8")
#print(str(wgetoutput))
#wgetline = re.search("(?P<url>hqdefault[^\s]+)", wgetoutput).group('url')
#translation_table = dict.fromkeys(map(ord, '‘’'), None)
#wgetfinal = wgetline.translate(translation_table)
#print(str(wgetfinal))
#subprocess.run(['dwebp', str(wgetfinal)])
