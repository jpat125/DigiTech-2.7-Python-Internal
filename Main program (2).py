#main program v2

from dis import dis
from lib2to3.pgen2 import driver
from unicodedata import mirrored
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




#resource db to go here:

websites = {
"KAMAR":"https://drive.google.com/file/d/16K9lJfnL3C9IF913k29JYJDTiXMdrtNS/view",
"google classroom":"https://drive.google.com/file/d/1uAGse14fctRMNYP-3t28VuKLi79Y5XAq/view",
"google drive":"https://support.google.com/drive/?hl=en#topic=14940",
"google docs/slides":"https://support.google.com/docs/?hl=en#topic=1382883"}


wificonnecting = {
"win/ipad":"https://drive.google.com/file/d/1jPfGX0knT0gAQYvaS7phYlL1D7onEiCx/view?usp=sharing",
"macOS":"https://drive.google.com/file/d/1avw7-i5diAHQ6UPG6en7E9PQ999W1LiY/view"
}

wifiremain = {
"win10":"link",
"win11":"link",
"macOS":"link",
"iPadOS":"link"}


displaymirroring = {
"win10":"link",
"win11":"link",
"macOS":"link",
"iPadOS":"link"}

displaymonitor = {
"win10":"https://drive.google.com/file/d/11cTYSBwgbVK_A3CK0hyCAuHVPsX62OoV/view?usp=sharing",
"win11":"https://drive.google.com/file/d/1XJcZodhqdsZootrNOwhm0yENvMtlNec8/view?usp=sharing",
"macOS":"https://drive.google.com/file/d/1rcsKU7H14xK5pZoheyIC0-aI5S3J88Vs/view?usp=sharing",
"iPadOS":"link"}


audioconnect = {
"win10":"https://drive.google.com/file/d/1KnkxN617MFcKG_Yo95xtZw4vE7tO0c1h/view?usp=sharing",
"win11":"https://drive.google.com/file/d/1FehHSMAIIBheyqeIJqlIE9c0utXIstOt/view?usp=sharing",
"macOS":"https://drive.google.com/file/d/1FOhVpn30CN4Fj0DJwkFZpoR2HB9Qkij2/view?usp=sharing",
}

printPIN = {
"printpin":"https://drive.google.com/file/d/1_c7usYyc0CTCGd8SgoJAvnoGQXVf0Djg/view"}

print = {
"print":"https://drive.google.com/file/d/1_c7usYyc0CTCGd8SgoJAvnoGQXVf0Djg/view"}


#helpdesk email
helpdesk = ("helpdesk@mags.school.nz")

#webq1
def whichweb():
     while True:
        whichweb=(int(input("""Please select an option below:
1 - KAMAR
2 - Google Classroom
3 - Google Drive  
4 - Google docs/slides
5 - Other

""").strip().lower()))
        if whichweb == 1:
            print ("'KAMAR' selected")
        elif whichweb == 2:
            print ("'Google Classroom' selected")
        elif whichweb == 3:
            print("'Google Drive' selected")
        elif whichweb == 4:
            print ("'Google doc/slides' selected")
        elif whichweb == 5:
            print ("'other' selected")
        else:
            print ("Unrecognised input, please try again")

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (whichweb == 1 or whichweb == 2 or  whichweb == 3 or  whichweb == 4 or  whichweb == 5):
            print ("Continuing")
            print ('\n')
            
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')
                                
        else:
            print("Unrecognised input")  
            print ('\n')
        
        if whichweb == 1:
            webbrowser.open(websites["KAMAR"])
            exit()
        elif whichweb == 2:
            webbrowser.open(websites["google classroom"])
            exit()
        elif whichweb == 3:
            webbrowser.open(websites["google drive"])
            exit()
        elif whichweb == 4:
            webbrowser.open(websites["google docs/slides"])
            exit()
        elif whichweb == 5:
            googlesearch()
            exit()
        else:
            ()


#def asks user for the type of device that is having the issue
def devicetype():
    while True:
        global devty
        devty=(int(input("""Please type out the number next to the type of device you are having an issue with:

1 - Laptop
2 - Ipad (Apple only)
3 - Tablet
4 - Apple Mac
5 - Other

*Press enter after typing*

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
        deviceosv=(input("What is the Operating System of the device? eg. Windows 10, IpadOS, macOS (if unknown, type 'uknown') *Press enter after typing* ").strip().lower().replace(" ", ""))
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

*Press enter after typing*

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

        if (displayissue == 1) and (deviceosv == "macOS"):
            webbrowser.open ("https://drive.google.com/file/d/1_eXdfVO4nRM_LLPizo9hWQtqul91OAbw/view?usp=sharing")
        else:
            print ("Chosen device OS not compatible with this option")

        if (displayissue == 2) and (deviceosv == "macOS"):
            webbrowser.open(displaymirroring["macOS"])
        elif (displayissue == 2) and (deviceosv == "windows 10"):
            webbrowser.open(displaymirroring["win10"])
        elif (displayissue == 2) and (deviceosv == "windows 11"):
            webbrowser.open(displaymirroring["win11"])
        else:
            print ("Chosen device OS not compatible with this option")
        if (displayissue == 3) and (deviceosv == "macOS"):
            webbrowser.open(displaymonitor["macOS"])
        elif (displayissue == 3) and (deviceosv == "windows 10"):
            webbrowser.open(displaymonitor["win10"])
        elif (displayissue == 3) and (deviceosv == "windows 11"):
            webbrowser.open(displaymonitor["win11"])
        else:
            print ("Chose device OS not compatible with this option")

        if displayissue == 4:
            googlesearch()
        else:
            ()

#deviceQ1
def devq1():
    
    while True:
        global devq1v
        devq1v = (int(input("""Please type the number of one of the options below:
1 - Display issue (including projecting)
2 - Wi-Fi issues
3 - Printing issues
4 - Audio issues
5 - Error code(s)
6 - Other

*Press enter after typing*

""").strip().lower()))
        if devq1v == 1:
            return (displayissue())#leads to display issues question
        elif devq1v == 2:
            return (wifissue())#leads to wifi issues question
        elif devq1v == 3:
            return (printissue())#leads to print issues issues question
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

*Press enter after typing*

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

        if (audioissuev == 1) and (deviceosv == "windows 10"):
            webbrowser.open(audioconnect["win10"])
        elif (audioissuev == 1) and (deviceosv == "windows 11"):
            webbrowser.open(audioconnect["win11"])
        elif (audioissuev == 1) and (deviceosv == "macOS"):
            webbrowser.open(audioconnect["macOS"])
        else:
            print ("Chosen device OS not compatible with this option")

        if (audioissuev == 2) and (deviceosv == "windows 10"):
            webbrowser.open(audioconnect["win10"])
        elif (audioissuev == 2) and (deviceosv == "windows 11"):
            webbrowser.open(audioconnect["win11"])
        elif (audioissuev == 2) and (deviceosv == ["macOS"]):
            webbrowser.open(audioconnect["macos"])
        else:
            print ("Chosen device OS not compatible with this option")
#wifi issue
def wifissue():
    while True:
        wifiissuev=(int(input("""I am having issues with:
1 - Connecting
2 - Other

*Press enter after typing*

""")))
        if wifiissuev == 1:
            print ("connecting issues")
            
        elif wifiissuev == 2:
            print("Other")
        
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

        if (wifiissuev == 1) and (deviceosv == "MacOS"):
            webbrowser.open(wificonnecting["macOS"])
        elif (wifiissuev == 1) and deviceosv == "windows 10" or (deviceosv == "windows 11") or (deviceosv == "ipadOS"):
            webbrowser.open(wificonnecting["win/ipad"])
        else:
            ()
        
        if (wifiissuev ==2):
            googlesearch()
#print issue
def printissue():
    while True:
        printissuev=(int(input("""I am having issues with:
1 - Setting printing PIN
2 - Printing in Black & White/Colour
3 - Other

*Press enter after typing*

""")))
        if printissuev == 1:
            print ("'Printing PIN issue' selected")
            
        elif printissuev == 2:
            print("'Printing issue' selected")
            
        elif printissuev == 3:
            print ("'Other' selected")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (printissuev == 1 or printissuev ==  2 or printissuev ==  3):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')

        if printissue == 1:
            webbrowser.open(printPIN["printpin"])
            exit()
        elif printissue == 2:
            webbrowser.open(print["print"])
            exit()
        elif printissue == 3:
            print (helpdesk)
        else:
            ()





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







PIN_access()
initalquestion()
deviceos()
devq1()
