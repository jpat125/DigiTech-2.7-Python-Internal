import webbrowser
import time
#Github commit test
def pin():
    while True:
        upin=(int(input("Please enter PIN: ")))
        if upin == (1234):
            print ("Acesss granted")
            break
        else:print("\nPlease try again")
    

def intitalquestion():
    iq1=int(input("""Hi there, how can I help you? 
 Options:
    1 = I have an issue with a device or website
    2 = I would like to submit an ICT Helpdesk ticket
    3 = I would like to close this program
    
    """
    
    ))
    if iq1 == 1:
        print ("1")
        devorweb()
    elif iq1 == 2:
        print("2")
    elif  iq1 == 3:
        print("Closing program...")
        time.sleep(3)
        exit()
    else:
        print ("I'm sorry, I don't seem to understand what your saying")

def devorweb():
    devorweb=(input("""Is the issue related to a:
1 = Device
2 = Website"""))

    if devorweb == "1":
        print ("device")
        devicetype()
    elif devorweb == "2":
        print ("Website")
        whichweb()
    else:
        print ("?")

def whichweb():
    whichweb=(int(input(""" Please select an option below:
1 - KAMAR
2 - Google Clasroom
3 - Google docs/slides
4 - 
""")))
    if whichweb =="1":
        print ("KAMAR selected")
    elif whichweb == "2":
        print ("Google Classroom")
    elif whichweb == "3":
        print ("Googgle doc/slides")


def devicetype():
    devicetype=int(input("What is the type of device? eg. Ipad or Laptop").lower().strip())
    if devicetype == "ipad":
        ()
    elif devicetype =="laptop":
        ()
    else:
        print ("I'm sorry, I don't seem to have that...")

def deviceos():
    global deviceosv
    deviceosv=(input("What is the Operating System of the device? eg. Windows 10 or IpadOS (if unknown, type 'uknown'").strip().lower())
    if deviceosv == "windows 10":
        print ("Windows 10")
    elif deviceosv =="windows 11":
        print ("Windows 11")
    elif deviceosv == "ipados":
        print ("IpadOS")
    elif deviceosv == "ios":
        print ("IOS")
    else:
        print ("That doesn't seem to be a supported Operating System, perphaps you have mispelt?")


def devq1():
    global devq1v
    devq1v = (int(input("""Please select one of the options below:
1 - Display issue (including projecting)
2 - Wi-Fi issues
3 - File issues
4 - Audio issues""")))
    if devq1v == 1:
        displayissue()
    elif devq1v == 2:
        wifissue()
    elif devq1v == 3:
        print ("file issues")
    elif devq1v == 4:
        print ("audio issues")
    else:
        print ("Unrecognised input")
 
def displayissue():
    displayissue=(int(input("""Please selct an option that best represents your display issue:
1 - Issue with casting 
2 - Issue with  
""")))

def wifissue():
    wifiissuev=(int(input("""I am having issues with:
 1 - Connecting
 2 - Remaining connected""")))
    if wifiissuev =="1":
        print ("connecting issues")
    elif wifiissuev =="2":
        print("remaining connected issue")


def googlesearch():
    taburl=("https://www.google.com/search?q=")
    querey=(input("Input query: "))
    search=(taburl+querey)
    webbrowser.open(search)


pin()
intitalquestion()
devq1()
deviceos()