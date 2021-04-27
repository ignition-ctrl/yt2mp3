import re
import requests
import subprocess

with open('results.txt') as f:
    for line in f:
        proc = subprocess.Popen(
            ['youtube-dl', '--list-thumbnails', line], stdout=subprocess.PIPE)
        youtubedl_output, err = proc.communicate()
        imgurl = re.search(
            "(?P<url>https?://[^\s]+)", youtubedl_output).group('url')
        
        r = requests.get(imgurl)
        if r.status_code == 200:
            with open(imgurl.split('/')[4] + '.jpg', 'wb') as file:
                for chunk in r.iter_content(1024):
                    file.write(chunk)
        else:
            print("Error with http")
