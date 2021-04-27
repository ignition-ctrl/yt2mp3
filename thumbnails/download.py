import subprocess
import sys
import re

if len(sys.argv) <= 1:
    print("No Youtube link provided\nABORTING")
    exit(1)
link = str(sys.argv[1])

proc = subprocess.Popen(
    ['youtube-dl', '--list-thumbnails', link], stdout=subprocess.PIPE)

youtubedl_output, err = proc.communicate()
imgurl = re.search(
    # "/maxresdefault/g", youtubedl_output).group(1)
    "(?P<url>https?://[^\s]+)", youtubedl_output).group('url')
print(imgurl)
subprocess.run('wget', str(imgurl))
