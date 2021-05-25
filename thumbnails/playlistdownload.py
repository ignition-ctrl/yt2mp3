from downloadimg import download_thumbnail

with open('list.txt') as l:
    global linecount
    linecount = 0
    for line in l:
        linecount += 1
        try:
            download_thumbnail(line, ("eva-"+str(linecount)), 'yes')
            print("download success\n")
        except:
            print("download failure\n")
    l.close()
