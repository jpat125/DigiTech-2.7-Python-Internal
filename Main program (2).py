#main program v1
#from glob import glob

import webbrowser
import time

#pin def
def PIN_access():

    while True:
        global studentuserpin
        global staffuserpin
        global userpin
        studentuserpin = (1234)
        staffuserpin = (12345)
        userpin=int(input("Enter PIN: "))
        if userpin == studentuserpin:
            print ("MAGS Student access granted")
            print('\n')
            break
        elif userpin == staffuserpin:
            print ("MAGS Staff access granted")
            print ('\n')
            break
        else:
            print ("Please try again:")
            print ('\n')

#Create def to ask user inital question (issue with device or website?)
def initalquestion():
    while True:
        iq=(int(input("""Is your issue regarding a:

1 - Device
2 - Website

""")))
        print ('\n')
        if iq == 1:
            return (devicetype())
        elif iq == 2:
            return (whichweb()) 
        else:
            print ("Unrecognised input!")
        print ('\n')
        contq = input(("Do you wish to continue? (y or n) ").strip().lower())
        print ('\n')
        if (contq == "y" or contq == "yes") and (iq == 1 or iq == 2 or iq == 3 or iq == 4):    
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
                    print ("Stopping")
                    print ('\n')
                            
        else:
            print("Unrecognised input")  
            print ('\n')

#webq1
def whichweb():
     while True:
        whichweb=(int(input("""Please select an option below:
1 - KAMAR
2 - Google Clasroom
3 - Google Drive  
4 - Google docs/slides
5 - Other

""").strip().lower()))
        if whichweb == 1:
            print ("KAMAR selected")
        elif whichweb == 2:
            print ("Google Classroom")
        elif whichweb == 3:
            print("Google Drive")
        elif whichweb == 4:
            print ("Googgle doc/slides")
        elif whichweb == 5:
            print ("other")
        else:
            print ("Unrecognised input, please try again")

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (whichweb == 1 or whichweb == 2 or  whichweb == 3 or  whichweb == 4 or  whichweb == 5):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')
                                
        else:
            print("Unrecognised input")  
            print ('\n')


#def asks user for the type of device that is having the issue
def devicetype():
    while True:
        global devty
        devty=(int(input("""Please select the type of device you are having an issue with:

1 - Laptop
2 - Ipad (Apple only)
3 - Tablet
4 - Apple Mac
5 - Other

""")))

        if devty == 1:
            print ("You have selected: Laptop")
        elif devty == 2:
            print ("You have selected: Ipad")
        elif devty == 3:
            print ("You have selected: Tablet")
        elif devty == 4:
            print ("You have selected: Apple Mac")
        elif devty == 5:
            print ("You have selected: Other")
        else:
            print ("Unrecognised input")

        print('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (devty == 1 or  devty == 2 or  devty == 3 or  devty == 4 or  devty == 5):   
            print ("Continuing")
            print ('\n')
            break
        
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')
            
        else:
            print("Unrecognised input")   
            print ('\n')

#devOS
def deviceos():
    global deviceosv
    
    while True:
        deviceosv=(input("What is the Operating System of the device? eg. Windows 10, IpadOS, macOS (if unknown, type 'uknown') ").strip().lower().replace(" ", ""))
        if deviceosv == "windows10":
            print ("Windows 10")
        elif deviceosv =="windows11":
           print ("Windows 11")
        elif deviceosv == "ipados":
            print ("IpadOS")
        elif deviceosv == "ios":
            print ("IOS")
        elif deviceosv == "macos":
            print ("macOS")
        elif deviceosv == "other":
            print ("Other")
        elif deviceosv == "unknown":
            print ("unknown")
        else:
            print ("That doesn't seem to be a supported Operating System, perphaps you have mispelt?")
            
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if contq == "y" or contq == "yes":
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
                print ("Stopping")
                print ('\n')
                        
        else:
            print("Unrecognised input")  
            print ('\n')

#display issue
def displayissue():
    while True:
        displayissue=(int(input("""Please type the number that best represents your display issue:
    1 - Issue with Apple TV
    2 - Issue with mirroring 
    3 - Issue with connecting to monitor/projector
    4 - Other 

    """)))
        if (displayissue == 1) and (userpin == staffuserpin):
            print ("Apple TV")

        elif displayissue == 2:
            print ("Mirroring")
        elif displayissue == 3:
            print ("Monitor")
        elif displayissue == 4:
            print ("Other")
        else:
            print("Either you don't have access to this or you have input an unrecognised input, please try again")


            
        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        
        print ('\n')
        if contq == "y" or contq == "yes" and displayissue == 1 or displayissue == 2 or displayissue == 3 or displayissue == 4 :
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')

#deviceQ1
def devq1():
    
    while True:
        global devq1v
        devq1v = (int(input("""Please select one of the options below:
1 - Display issue (including projecting)
2 - Wi-Fi issues
3 - File issues
4 - Audio issues
5 - Error code(s)
6 - Other

""").strip().lower()))
        if devq1v == 1:
            return (displayissue())#leads to display issues question
        elif devq1v == 2:
            return (wifissue())#leads to wifi issues question
        elif devq1v == 3:
            return (fileissue())#leads to file issues issues question
        elif devq1v == 4:
            return (audioissue())#leads to audio issues question
        elif devq1v == 5:
            return (errorcodesearch())#leads to google search
        elif devq1v == 6:
            return (googlesearch())#lead to google search
        else:
            print ("Unrecognised input")
        
        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (devq1v == 1 or devq1v == 2 or devq1v == 3 or devq1v == 4):    
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
                    print ("Stopping")
                    print ('\n')
                            
        else:
            print("Unrecognised input")  
            print ('\n')

#audio issue
def audioissue():
    while True:
        audioissuev=(int(input("""I am having issues with:
1 - Connecting to projector or TV
2 - Connecting to speakers
3 - Other

""")))
        if audioissuev == 1:
            print ("connecting to projector/tv")
            
        elif audioissuev == 2:
            print("connecting to speakers")
            
        elif audioissuev == 3:
            print ("Other")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (audioissuev == 1 or audioissuev ==  2 or audioissuev ==  3):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')
#wifi issue
def wifissue():
    while True:
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
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (wifiissuev == 1 or wifiissuev ==  2 or wifiissuev ==  3):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')
#file issue
def fileissue():
    while True:
        fileissuev=(int(input("""I am having issues with:
1 - Zipping & Un-zipping files
2 - Onedrive
3 - Other

""")))
        if fileissuev == 1:
            print ("Zipping & unzipping")
            
        elif fileissuev == 2:
            print("Onedrive")
            
        elif fileissuev == 3:
            print ("Other")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (fileissuev == 1 or fileissuev ==  2 or fileissuev ==  3):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')
#google search
def googlesearch():
    taburl=("https://www.google.com/search?q=")
    querey=(input("Input query: "))
    search=(taburl+querey)
    webbrowser.open(search)
    time.sleep (1.5)
#error code
def errorcodesearch():
    taburl=("https://www.google.com/search?q=")
    errorcode=(input("Input error code: "))
    search=(taburl+"Error code "+errorcode+" "+deviceosv)
    webbrowser.open(search)
    time.sleep (1.5)


#resource db to go here:









PIN_access()
initalquestion()
deviceos()
devq1()