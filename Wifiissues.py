def wifissue():
    wifiissuev=(int(input("""I am having issues with:
 1 - Connecting
 2 - Remaining connected
 3 - Other
 """)))
    if wifiissuev == 1:
        print ("connecting issues")
    elif wifiissuev == 2:
        print("remaining connected issue")
    elif wifiissuev == 3:
        print ("Other")

wifissue()