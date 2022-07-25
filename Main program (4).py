#main program v2

import webbrowser
import time
import pyperclip
import os
import emoji

#/*  .oooooo.                             .                           .              .o8                                  oooo                                          
#d8P'  `Y8b                          .o8                         .o8             "888                                  `888                                          
#888           .ooooo.  ooo. .oo.   .o888oo  .oooo.    .ooooo.  .o888oo       .oooo888   .ooooo.  oooo    ooo  .ooooo.   888   .ooooo.  oo.ooooo.   .ooooo.  oooo d8b 
#888          d88' `88b `888P"Y88b    888   `P  )88b  d88' `"Y8   888        d88' `888  d88' `88b  `88.  .8'  d88' `88b  888  d88' `88b  888' `88b d88' `88b `888""8P 
#888          888   888  888   888    888    .oP"888  888         888        888   888  888ooo888   `88..8'   888ooo888  888  888   888  888   888 888ooo888  888     
#`88b    ooo  888   888  888   888    888 . d8(  888  888   .o8   888 .      888   888  888    .o    `888'    888    .o  888  888   888  888   888 888    .o  888     
# `Y8bood8P'  `Y8bod8P' o888o o888o   "888" `Y888""8o `Y8bod8P'   "888"      `Y8bod88P" `Y8bod8P'     `8'     `Y8bod8P' o888o `Y8bod8P'  888bod8P' `Y8bod8P' d888b    
#                                                                                                                                        888                          
#                                                                                                                                       o888o                         

devemail_emoji=(emoji.emojize(':e-mail:'))
mistake=(f"If you belive I have made a mistake, please contact my devloper at: jpatel@students.mags.school.nz {devemail_emoji}")
    






#/*oooooooooooo                                 o8o  o8o           
#`888'     `8                                 `"'  `"'           
# 888         ooo. .oo.  .oo.    .ooooo.     oooo oooo   .oooo.o 
# 888oooo8    `888P"Y88bP"Y88b  d88' `88b    `888 `888  d88(  "8 
# 888    "     888   888   888  888   888     888  888  `"Y88b.  
# 888       o  888   888   888  888   888     888  888  o.  )88b 
#o888ooooood8 o888o o888o o888o `Y8bod8P'     888 o888o 8""888P' 
#                                             888                
#                                         .o. 88P                
#                                         `Y888P          

error_emoji=(emoji.emojize(':red_exclamation_mark:'))





# /*ooooooooo.   ooooo ooooo      ooo                                                                
# `888   `Y88. `888' `888b.     `8'                                                                
#  888   .d88'  888   8 `88b.    8        .oooo.    .ooooo.   .ooooo.   .ooooo.   .oooo.o  .oooo.o 
#  888ooo88P'   888   8   `88b.  8       `P  )88b  d88' `"Y8 d88' `"Y8 d88' `88b d88(  "8 d88(  "8 
#  888          888   8     `88b.8        .oP"888  888       888       888ooo888 `"Y88b.  `"Y88b.  
#  888          888   8       `888       d8(  888  888   .o8 888   .o8 888    .o o.  )88b o.  )88b 
# o888o        o888o o8o        `8       `Y888""8o `Y8bod8P' `Y8bod8P' `Y8bod8P' 8""888P' 8""888P' 

#pin def
def PIN_access():
    
    global studentuserpin
    global staffuserpin
    global userpin

    while True:   
            wave = (emoji.emojize(':waving_hand:'))
            print (wave, "Hi there!\nThis is an automated IT support tool for Mount Albert Grammar School staff and students.")
    
            userpin = (input("Enter your PIN:  "))


            checki=(userpin.isnumeric())

            studentuserpin = "1234"
            staffuserpin = "12345"

           
            
            if (userpin == studentuserpin) and (checki==True):
                print ("MAGS Student access granted")
                print('\n')
                break
            elif (userpin == staffuserpin) and (checki==True):
                print ("MAGS Staff access granted")
                print ('\n')
                break
            else:
                print ("Incorrect input, please try again:")
                print ('\n')


# /*ooooo              o8o      .             oooo                                                     .    o8o                        
# `888'              `"'    .o8             `888                                                   .o8    `"'                        
#  888  ooo. .oo.   oooo  .o888oo  .oooo.    888        .ooooo oo oooo  oooo   .ooooo.   .oooo.o .o888oo oooo   .ooooo.  ooo. .oo.   
#  888  `888P"Y88b  `888    888   `P  )88b   888       d88' `888  `888  `888  d88' `88b d88(  "8   888   `888  d88' `88b `888P"Y88b  
#  888   888   888   888    888    .oP"888   888       888   888   888   888  888ooo888 `"Y88b.    888    888  888   888  888   888  
#  888   888   888   888    888 . d8(  888   888       888   888   888   888  888    .o o.  )88b   888 .  888  888   888  888   888  
# o888o o888o o888o o888o   "888" `Y888""8o o888o      `V8bod888   `V88V"V8P' `Y8bod8P' 8""888P'   "888" o888o `Y8bod8P' o888o o888o 
#                                                            888.                                                                    
#                                                            8P'                                                                     
#                                                            "                                                                    

#Create def to ask user inital question (issue with device or website?)
def initalquestion():
    global iq
    
    while True:
            #device_emoji=(emoji.emojize(':desktop_computer:'))
            #web_emoji=(emoji.emojize(':globe_with_meridians:'))
            iq=(input("""Is your issue regarding a:

1 - BYOD, School or Staff Device 
2 - Website 

"""))

            
            if iq == "1":
                print (f"You have selected: Issue with a Device")
            elif iq == "2":
                print (f"You have selected: Issue with a Website") 
            else:
                print (f"{error_emoji}I'm sorry, I don't think that's an option!\n"+mistake)
            print ('\n')

            if iq == "1" or iq =="2":
                contq = input(("Do you wish to continue? (y or n) ").strip().lower())
                print ('\n')
                if (contq == "y" or contq == "yes"):    
                    print ("Continuing")
                    print ('\n')
                    if iq == "1":
                        return (devicetype())
                    elif iq == "2":
                        return (whichweb())
               
                    
                elif contq == "n" or contq == "no":
                            print ("Stopping")
                            print ('\n')     
                                          
                else:
                    print(f"{error_emoji}Unrecognised input {error_emoji}")
                    print ('\n')

              


#resource db to go here:

# /*ooooooooo.                                                                                  
# `888   `Y88.                                                                                
#  888   .d88'  .ooooo.   .oooo.o  .ooooo.  oooo  oooo  oooo d8b  .ooooo.   .ooooo.   .oooo.o 
#  888ooo88P'  d88' `88b d88(  "8 d88' `88b `888  `888  `888""8P d88' `"Y8 d88' `88b d88(  "8 
#  888`88b.    888ooo888 `"Y88b.  888   888  888   888   888     888       888ooo888 `"Y88b.  
#  888  `88b.  888    .o o.  )88b 888   888  888   888   888     888   .o8 888    .o o.  )88b 
# o888o  o888o `Y8bod8P' 8""888P' `Y8bod8P'  `V88V"V8P' d888b    `Y8bod8P' `Y8bod8P' 8""888P' 
                                                                                            
                                                                                            
                                                                                    
websites = {
"KAMAR":"https://drive.google.com/file/d/16K9lJfnL3C9IF913k29JYJDTiXMdrtNS/view",
"google classroom":"https://drive.google.com/file/d/1uAGse14fctRMNYP-3t28VuKLi79Y5XAq/view",
"google drive":"https://support.google.com/drive/?hl=en#topic=14940",
"google docs/slides":"https://support.google.com/docs/?hl=en#topic=1382883"}



#"https://drive.google.com/file/d/1jPfGX0knT0gAQYvaS7phYlL1D7onEiCx/view?usp=sharing",

#"https://drive.google.com/file/d/1avw7-i5diAHQ6UPG6en7E9PQ999W1LiY/view"



displaymirroring = {
"win10/11":"https://drive.google.com/file/d/1Lcqxyu1V3Ux5n3U7_t3FQlk_shnTFlem/view?usp=sharing",
"macOS":"https://drive.google.com/file/d/1cf2DiJSysehx9bMe8kMZXQsfhKdwsHwl/view?usp=sharing"
}

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

printing = {
"print":"https://drive.google.com/file/d/1_c7usYyc0CTCGd8SgoJAvnoGQXVf0Djg/view"}



# /*ooooo   ooooo           oooo                   .o8                     oooo                                                    o8o  oooo  
# `888'   `888'           `888                  "888                     `888                                                    `"'  `888  
#  888     888   .ooooo.   888  oo.ooooo.   .oooo888   .ooooo.   .oooo.o  888  oooo        .ooooo.  ooo. .oo.  .oo.    .oooo.   oooo   888  
#  888ooooo888  d88' `88b  888   888' `88b d88' `888  d88' `88b d88(  "8  888 .8P'        d88' `88b `888P"Y88bP"Y88b  `P  )88b  `888   888  
#  888     888  888ooo888  888   888   888 888   888  888ooo888 `"Y88b.   888888.         888ooo888  888   888   888   .oP"888   888   888  
#  888     888  888    .o  888   888   888 888   888  888    .o o.  )88b  888 `88b.       888    .o  888   888   888  d8(  888   888   888  
# o888o   o888o `Y8bod8P' o888o  888bod8P' `Y8bod88P" `Y8bod8P' 8""888P' o888o o888o      `Y8bod8P' o888o o888o o888o `Y888""8o o888o o888o 
#                                888                                                                                                        
#                               o888o                                                                                                       

#helpdesk email
def helpdesk():
    helpdesk_emoji =(emoji.emojize(':technologist:'))
    print (helpdesk_emoji)
    email=("helpdesk@mags.school.nz")
    pyperclip.copy(email)
    print (email)
    print ("*email address copied to clipboard*")
    print ('\n')

    
# /*oooooo   oooooo     oooo oooo         o8o            oooo                                         .o8                 o8o      .             
#  `888.    `888.     .8'  `888         `"'            `888                                        "888                 `"'    .o8             
#   `888.   .8888.   .8'    888 .oo.   oooo   .ooooo.   888 .oo.        oooo oooo    ooo  .ooooo.   888oooo.   .oooo.o oooo  .o888oo  .ooooo.  
#    `888  .8'`888. .8'     888P"Y88b  `888  d88' `"Y8  888P"Y88b        `88. `88.  .8'  d88' `88b  d88' `88b d88(  "8 `888    888   d88' `88b 
#     `888.8'  `888.8'      888   888   888  888        888   888         `88..]88..8'   888ooo888  888   888 `"Y88b.   888    888   888ooo888 
#      `888'    `888'       888   888   888  888   .o8  888   888          `888'`888'    888    .o  888   888 o.  )88b  888    888 . 888    .o 
#       `8'      `8'       o888o o888o o888o `Y8bod8P' o888o o888o          `8'  `8'     `Y8bod8P'  `Y8bod8P' 8""888P' o888o   "888" `Y8bod8P' 



#webq1
def whichweb():
     while True:
        whichweb=(input("""Please select an option below:
1 - KAMAR
2 - Google Classroom
3 - Google Drive  
4 - Google docs/slides
5 - Other

""").strip().lower())



        if whichweb == "1":
            print ("'KAMAR' selected")
        elif whichweb == "2":
            print ("'Google Classroom' selected")
        elif whichweb == "3":
            print("'Google Drive' selected")
        elif whichweb == "4":
            print ("'Google doc/slides' selected")
        elif whichweb == "5":
            print ("'other' selected")
        else:
            print ("Unrecognised input, please try again")

        print ('\n')
        
        if whichweb == "1" or whichweb =="2" or whichweb =="3" or whichweb=="4" or whichweb=="5":
            contq = input("Have you selected the correct option? (y or n) ").strip().lower()
            print ('\n')
            if (contq == "y" or contq == "yes"):
                if whichweb == "1":
                    webbrowser.open(websites["KAMAR"])
                    exit()
                elif whichweb == "2":
                    webbrowser.open(websites["google classroom"])
                    exit()
                elif whichweb == "3":
                    webbrowser.open(websites["google drive"])
                    exit()
                elif whichweb == "4":
                    webbrowser.open(websites["google docs/slides"])
                    exit()
                elif whichweb == "5":
                    googlesearch()
                    
                else:
                    ()
                print ("Continuing")
                print ('\n')
                
            elif contq == "n" or contq == "no":
                print ("Stopping")
                print ('\n')
                                    
            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")  
                print ('\n')
            
            
# /*oooooooooo.                          o8o                          .                                    
# `888'   `Y8b                         `"'                        .o8                                    
#  888      888  .ooooo.  oooo    ooo oooo   .ooooo.   .ooooo.  .o888oo oooo    ooo oo.ooooo.   .ooooo.  
#  888      888 d88' `88b  `88.  .8'  `888  d88' `"Y8 d88' `88b   888    `88.  .8'   888' `88b d88' `88b 
#  888      888 888ooo888   `88..8'    888  888       888ooo888   888     `88..8'    888   888 888ooo888 
#  888     d88' 888    .o    `888'     888  888   .o8 888    .o   888 .    `888'     888   888 888    .o 
# o888bood8P'   `Y8bod8P'     `8'     o888o `Y8bod8P' `Y8bod8P'   "888"     .8'      888bod8P' `Y8bod8P' 
#                                                                       .o..P'       888                                                                                     `Y8P'       o888o                
#def asks user for the type of device that is having the issue

def devicetype():
    global devty
    while True:
        devty=(input("""Please type out the number next to the type of device you are having an issue with:

1 - Laptop
2 - Ipad (Apple only)
3 - Tablet
4 - Apple Mac
5 - Other

*Press enter after typing*

"""))

        if devty == "1":
            print ("You have selected: Laptop")
            
        elif devty == "2":
            print ("You have selected: Ipad")
            
        elif devty == "3":
            print ("You have selected: Tablet")
            
        elif devty == "4":
            print ("You have selected: Apple Mac")
            
        elif devty == "5":
            print ("You have selected: Other")
            print("I'm sorry, I don't have resources to help you, I recommend you contact IT helpdesk")
            helpdesk()
            print ("\n")
            exit()
            
        else:
            print (f"{error_emoji}Unrecognised input{error_emoji}")

        print('\n')

        if devty =="1" or devty=="2" or devty=="3" or devty=="4" or devty=="5":
            contq = input("Have you selected the correct option? (y or n) ").strip().lower()
            print ('\n')
            if (contq == "y" or contq == "yes") and (devty == "1" or devty == "2" or devty == "3" or devty == "4" or devty == "5"):   
                print ("Continuing")
                print ('\n')
                break
                exit()
            
            elif contq == "n" or contq == "no":
                print ("Stopping")
                print ('\n')
                
            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")   
                print ('\n')
        else:
            ()   

# /*oooooooooo.                          o8o                        .oooooo.    .oooooo..o 
# `888'   `Y8b                         `"'                       d8P'  `Y8b  d8P'    `Y8 
#  888      888  .ooooo.  oooo    ooo oooo   .ooooo.   .ooooo.  888      888 Y88bo.      
#  888      888 d88' `88b  `88.  .8'  `888  d88' `"Y8 d88' `88b 888      888  `"Y8888o.  
#  888      888 888ooo888   `88..8'    888  888       888ooo888 888      888      `"Y88b 
#  888     d88' 888    .o    `888'     888  888   .o8 888    .o `88b    d88' oo     .d8P 
# o888bood8P'   `Y8bod8P'     `8'     o888o `Y8bod8P' `Y8bod8P'  `Y8bood8P'  8""88888P'  
#devOS


def deviceos():
    global deviceoss
    
    while True:
        deviceosv=(input("What is the Operating System of the device? eg. Windows 10, IpadOS, macOS (if unknown, type 'uknown') *Press enter after typing* ").strip().lower().replace(" ", ""))
        deviceoss=()
        if deviceosv == "windows10" or deviceosv == "win10":
            deviceoss = ("windows10")
            print ("Windows 10")
            print (deviceoss)
        elif deviceosv =="windows11" or deviceosv == "win11":
            deviceoss =("windows11")
            print ("Windows 11")
        elif deviceosv == "ipados" or deviceosv == "ipad":
            deviceoss =("ipados")
            print ("IpadOS")
        elif deviceosv == "macos" or deviceosv == "mac":
            deviceoss =("macos")
            print ("macOS")
        elif deviceosv == "unknown" or deviceosv == "other": 
            print (helpdesk)
        else:
            print (f"{error_emoji}That doesn't seem to be a supported Operating System, perphaps you have mispelt?{error_emoji}")
            print ('\n')
        if deviceoss == "macos" or deviceoss == "windows10" or deviceoss =="windows11" or deviceoss == "ipados":
            contq = input("Have you selected the correct option? (y or n) ").strip().lower()
            print ('\n')
            if contq == "y" or contq == "yes":
                print ("Continuing")
                print ('\n')
                break
            elif contq == "n" or contq == "no":
                    print ("Stopping")
                    print ('\n')
                            
            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")  
                print ('\n')
    else:
        ()
# /*oooooooooo.                                      .o  
# `888'   `Y8b                                   o888  
#  888      888  .ooooo.  oooo    ooo  .ooooo oo  888  
#  888      888 d88' `88b  `88.  .8'  d88' `888   888  
#  888      888 888ooo888   `88..8'   888   888   888  
#  888     d88' 888    .o    `888'    888   888   888  
# o888bood8P'   `Y8bod8P'     `8'     `V8bod888  o888o 
#                                           888.       
#                                           8P'
#deviceQ1



def devq1():
    global devq1v
    while True:
            devq1v = (input("""Please type the number of one of the options below:
1 - Display issue (including projecting)
2 - Wi-Fi issues
3 - Printing issues
4 - Audio issues
5 - Error code(s)
6 - Other
7 - Contact Helpdesk

*Press enter after typing*

""").strip().lower())

            if devq1v == "1":
                print("Display issue selected")
            elif devq1v == "2":
                print ("Wi-Fi issue selevted")
            elif devq1v == "3":
                print ("Printing issue selected")
            elif devq1v == "4":
                print ("Audio issue selected")
            elif devq1v == "5":
                print ("Error code serach selected")
            elif devq1v =="6":
                print ("Other selected")
            elif devq1v =="7":
                print ("Contact Helpdesk selected")

            if devq1v  =="1" or devq1v  =="2" or devq1v  =="3" or devq1v  =="4" or devq1v  =="5" or devq1v =="6" or devq1v  =="7":         
                contq = input("Have you selected the correct option? (y or n) ").strip().lower()
                print ('\n')
                if (contq == "y" or contq == "yes"):
                    print ("Continuing")
                    print ('\n')
                    if devq1v == "1":
                        return (displayissue())#leads to display issues question
                    elif devq1v == "2":
                        return (wifissue())#leads to wifi issues question
                    elif devq1v == "3":
                        return (printissue())#leads to print issues issues question
                    elif devq1v == "4":
                        return (audioissue())#leads to audio issues question
                    elif devq1v == "5":
                        return (errorcodesearch())#leads to google search
                    elif devq1v == "6":
                        return (googlesearch())#lead to google search
                    elif devq1v == "7":
                        return (helpdesk())#throws up helpdesk email address
                    else:
                        print (f"{error_emoji}Unrecognised input{error_emoji}")
                    
                        print ('\n')

                elif contq == "n" or contq == "no":
                    print ("Stopping")
                    print ('\n')
                                    
                else:
                    print(f"{error_emoji}Unrecognised input{error_emoji}")  
                    print ('\n')

            

# /*oooooooooo.    o8o                      oooo                              o8o                                          
# `888'   `Y8b   `"'                      `888                              `"'                                          
#  888      888 oooo   .oooo.o oo.ooooo.   888   .oooo.   oooo    ooo      oooo   .oooo.o  .oooo.o oooo  oooo   .ooooo.  
#  888      888 `888  d88(  "8  888' `88b  888  `P  )88b   `88.  .8'       `888  d88(  "8 d88(  "8 `888  `888  d88' `88b 
#  888      888  888  `"Y88b.   888   888  888   .oP"888    `88..8'         888  `"Y88b.  `"Y88b.   888   888  888ooo888 
#  888     d88'  888  o.  )88b  888   888  888  d8(  888     `888'          888  o.  )88b o.  )88b  888   888  888    .o 
# o888bood8P'   o888o 8""888P'  888bod8P' o888o `Y888""8o     .8'          o888o 8""888P' 8""888P'  `V88V"V8P' `Y8bod8P' 
#                               888                       .o..P'                                                         
#                              o888o                      `Y8P'                                                          
#                                                                                                                        */
#display issue



def displayissue():
    while True:
            auth=('')
            displayissue=(input("""Please type the number that best represents your display issue:
    1 - Issue with Apple TV
    2 - Issue with mirroring
    3 - Issue with connecting to monitor/projector
    4 - Other 

*Press enter after typing*

"""))
            no_acess=device_emoji=(emoji.emojize(':no_entry:'))
            if (displayissue == "1") and (userpin == staffuserpin):
                print ("Apple TV selected")
            
            elif displayissue == "2":
                print ("mirroring selected")
            elif displayissue == "3":
                print ("Monitor selected")
            elif displayissue == "4":
                print ("Other selceted")
            else:
                print(f"{no_acess} Either you don't have access to this or you have input an unrecognised input, please try again {no_acess}")
                auth=("false")
            print ('\n')
            if displayissue == "1" or displayissue == "2" or  displayissue =="3" or displayissue=="4" and auth=="":
                contq = input("Have you selected the correct option? (y or n) ").strip().lower()
                
                print ('\n')
                if contq == "y" or contq == "yes" and displayissue == "1" or displayissue == "2" or displayissue == "3" or displayissue == "4":
                    print ("Continuing")
                    print ('\n')
                    
                elif contq == "n" or contq == "no":
                    print ("Stopping")
                    print ('\n')                
                else:
                    print(f"{error_emoji}Unrecognised input{error_emoji}")  
                    print ('\n')

                if (displayissue == "1") and (deviceoss == "macos"):
                    webbrowser.open ("https://drive.google.com/file/d/1_eXdfVO4nRM_LLPizo9hWQtqul91OAbw/view?usp=sharing")
                    exit()
                elif (displayissue == "2") and (deviceoss == "macos"):
                    webbrowser.open(displaymirroring["macOS"])
                    exit()
                elif (displayissue == "2") and (deviceoss == "windows10"):
                    webbrowser.open(displaymirroring["win10/11"])
                    exit()
                elif (displayissue == "2") and (deviceoss == "windows11"):
                    webbrowser.open(displaymirroring["win10/11"])
                    exit()
                elif (displayissue == "3") and (deviceoss == "macOS"):
                    webbrowser.open(displaymonitor["macOS"])
                    exit()
                elif (displayissue == "3") and (deviceoss == "windows10"):
                    webbrowser.open(displaymonitor["win10"])
                    exit()
                elif (displayissue == "3") and (deviceoss == "windows11"):
                    webbrowser.open(displaymonitor["win11"])
                    exit()
                elif displayissue == "4":
                    googlesearch()
                else:
                    print (f"{error_emoji}Chosen device OS not compatible with this option{error_emoji}")

                    
# /*      .o.                         .o8   o8o                 ooooo                                         
#      .888.                       "888   `"'                 `888'                                         
#     .8"888.     oooo  oooo   .oooo888  oooo   .ooooo.        888   .oooo.o  .oooo.o oooo  oooo   .ooooo.  
#    .8' `888.    `888  `888  d88' `888  `888  d88' `88b       888  d88(  "8 d88(  "8 `888  `888  d88' `88b 
#   .88ooo8888.    888   888  888   888   888  888   888       888  `"Y88b.  `"Y88b.   888   888  888ooo888 
#  .8'     `888.   888   888  888   888   888  888   888       888  o.  )88b o.  )88b  888   888  888    .o 
# o88o     o8888o  `V88V"V8P' `Y8bod88P" o888o `Y8bod8P'      o888o 8""888P' 8""888P'  `V88V"V8P' `Y8bod8P' 
                                                                                                          
#audio issue



def audioissue():
    while True:
    
        audioissuev=(input("""I am having issues with:
1 - Connecting to projector or TV
2 - Connecting to speakers
3 - Other

*Press enter after typing*

"""))
        if audioissuev == "1":
            print ("connecting to projector/tv")
            
        elif audioissuev == "2":
            print("connecting to speakers")
            
        elif audioissuev == "3":
            print ("Other")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')

        if audioissuev == "1" or audioissuev == "2" or audioissuev == "3":
            contq = input("Have you selected the correct option? (y or n) ").strip().lower()
            print ('\n')
            if (contq == "y" or contq == "yes") and (audioissuev == "1" or audioissuev ==  "2" or audioissuev ==  "3"):
                print ("Continuing")
                print ('\n')
                
            elif contq == "n" or contq == "no":
                print ("Stopping")
                print ('\n')                
            else:
                print("Unrecognised input")  
                print ('\n')

        if (audioissuev == "1") and (deviceoss == "windows10"):
            webbrowser.open(audioconnect["win10"])
            exit()
        elif (audioissuev == "1") and (deviceoss == "windows11"):
            webbrowser.open(audioconnect["win11"])
            exit()
        elif (audioissuev == "1") and (deviceoss == "macOS"):
            webbrowser.open(audioconnect["macOS"])
            exit()
        elif (audioissuev == "2") and (deviceoss == "windows10"):
            webbrowser.open(audioconnect["win10"])
            exit()
        elif (audioissuev == "2") and (deviceoss == "windows11"):
            webbrowser.open(audioconnect["win11"])
            exit()
        elif (audioissuev == 2) and (deviceoss == ["macOS"]):
            webbrowser.open(audioconnect["macOS"])
            exit()
        elif audioissuev == "3":
            helpdesk()
        else:
            print ("Chosen device OS not compatible with this option")

# /*oooooo   oooooo     oooo  o8o   .o88o.  o8o        o8o                                          
#  `888.    `888.     .8'   `"'   888 `"  `"'        `"'                                          
#   `888.   .8888.   .8'   oooo  o888oo  oooo       oooo   .oooo.o  .oooo.o oooo  oooo   .ooooo.  
#    `888  .8'`888. .8'    `888   888    `888       `888  d88(  "8 d88(  "8 `888  `888  d88' `88b 
#     `888.8'  `888.8'      888   888     888        888  `"Y88b.  `"Y88b.   888   888  888ooo888 
#      `888'    `888'       888   888     888        888  o.  )88b o.  )88b  888   888  888    .o 
#       `8'      `8'       o888o o888o   o888o      o888o 8""888P' 8""888P'  `V88V"V8P' `Y8bod8P' 


#wifi issue



def wifissue():
    while True:
        wifiissuev=(input("""I am having issues with:
1 - Connecting
2 - Other

*Press enter after typing*

"""))

        if wifiissuev == "1":
            print ("connecting issues")
        
        elif wifiissuev == "2":
            print("Other")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')

        if wifiissuev =="1" or wifiissuev =="2": 
            contq = input("Have you selected the correct option? (y or n) ").strip().lower()
            print ('\n')
            if (contq == "y" or contq == "yes") and (wifiissuev == "1" or wifiissuev ==  "2" or wifiissuev ==  "3"):
                print ("Continuing")
                print ('\n')
                
            elif contq == "n" or contq == "no":
                print ("Stopping")
                print ('\n')                
            else:
                print("Unrecognised input")  
                print ('\n')

        if (wifiissuev == "1") and (deviceoss == "Macos"):
            #webbrowser.open(wificonnecting["macOS"])
            f = open("Wifi connecting - students")
            exit()
        elif (wifiissuev == "1") and (deviceoss == "windows10") or (deviceoss == "windows11") or (deviceoss == "ipados"):
            path = os.path.basename('/2.7 Internal/To connect to School Wifi.pdf')
            os.startfile(path)
            
            exit()
        else:
            print("Either you don't have access to this or you have input an unrecognised input, please try again")
            

        if (wifiissuev =="2"):
            googlesearch()

# /*ooooooooo.             o8o                  .         o8o                                          
# `888   `Y88.           `"'                .o8         `"'                                          
#  888   .d88' oooo d8b oooo  ooo. .oo.   .o888oo      oooo   .oooo.o  .oooo.o oooo  oooo   .ooooo.  
#  888ooo88P'  `888""8P `888  `888P"Y88b    888        `888  d88(  "8 d88(  "8 `888  `888  d88' `88b 
#  888          888      888   888   888    888         888  `"Y88b.  `"Y88b.   888   888  888ooo888 
#  888          888      888   888   888    888 .       888  o.  )88b o.  )88b  888   888  888    .o 
# o888o        d888b    o888o o888o o888o   "888"      o888o 8""888P' 8""888P'  `V88V"V8P' `Y8bod8P' 
#print issue



def printissue():
    while True:
        
            printissuev=(input("""I am having issues with:
1 - Setting printing PIN
2 - Printing in Black & White/Colour
3 - Other

*Press enter after typing*

"""))

            if printissuev == "1":
                print ("'Printing PIN issue' selected")
                
            elif printissuev == "2":
                print("'Printing issue' selected")
                
            elif printissuev == "3":
                print ("'Other' selected")
            
            else:
                print ("Unrecognised input, please try again") 

            print ('\n')

            if printissuev=="1" or printissuev==2 or printissuev=="3":
                contq = input("Have you selected the correct option? (y or n) ").strip().lower()
                print ('\n')
                if (contq == "y" or contq == "yes") and (printissuev == "1" or printissuev ==  "2" or printissuev ==  "3"):
                    print ("Continuing")
                    print ('\n')
                    
                elif contq == "n" or contq == "no":
                    print ("Stopping")
                    print ('\n')                
                else:
                    print("Unrecognised input")  
                    print ('\n')

            if printissuev == "1":
                webbrowser.open(printPIN["printpin"])
                exit()
            elif printissuev == "2":
                webbrowser.open(printing["print"])
                exit()
            elif printissuev == "3":
                helpdesk()
            else:
                ()

# /*  .oooooo.                                   oooo                                                                 oooo        
#  d8P'  `Y8b                                  `888                                                                 `888        
# 888            .ooooo.   .ooooo.   .oooooooo  888   .ooooo.        .oooo.o  .ooooo.   .oooo.   oooo d8b  .ooooo.   888 .oo.   
# 888           d88' `88b d88' `88b 888' `88b   888  d88' `88b      d88(  "8 d88' `88b `P  )88b  `888""8P d88' `"Y8  888P"Y88b  
# 888     ooooo 888   888 888   888 888   888   888  888ooo888      `"Y88b.  888ooo888  .oP"888   888     888        888   888  
# `88.    .88'  888   888 888   888 `88bod8P'   888  888    .o      o.  )88b 888    .o d8(  888   888     888   .o8  888   888  
#  `Y8bood8P'   `Y8bod8P' `Y8bod8P' `8oooooo.  o888o `Y8bod8P'      8""888P' `Y8bod8P' `Y888""8o d888b    `Y8bod8P' o888o o888o 
#                                   d"     YD                                                                                   
#                                   "Y88888P'                                                                                   
#google search



def googlesearch():
    taburl=("https://www.google.com/search?q=")
    querey=(input("Input query: "))
    search=(taburl+querey)
    webbrowser.open(search)
    time.sleep (1.5)
    exit()

# /*oooooooooooo                                                                .o8                                                                 oooo        
# `888'     `8                                                               "888                                                                 `888        
#  888         oooo d8b oooo d8b  .ooooo.  oooo d8b  .ooooo.   .ooooo.   .oooo888   .ooooo.        .oooo.o  .ooooo.   .oooo.   oooo d8b  .ooooo.   888 .oo.   
#  888oooo8    `888""8P `888""8P d88' `88b `888""8P d88' `"Y8 d88' `88b d88' `888  d88' `88b      d88(  "8 d88' `88b `P  )88b  `888""8P d88' `"Y8  888P"Y88b  
#  888    "     888      888     888   888  888     888       888   888 888   888  888ooo888      `"Y88b.  888ooo888  .oP"888   888     888        888   888  
#  888       o  888      888     888   888  888     888   .o8 888   888 888   888  888    .o      o.  )88b 888    .o d8(  888   888     888   .o8  888   888  
# o888ooooood8 d888b    d888b    `Y8bod8P' d888b    `Y8bod8P' `Y8bod8P' `Y8bod88P" `Y8bod8P'      8""888P' `Y8bod8P' `Y888""8o d888b    `Y8bod8P' o888o o888o 

#error code



def errorcodesearch():
    taburl=("https://www.google.com/search?q=")
    errorcode=(input("Input error code: "))
    search=(taburl+"Error code "+errorcode+" "+deviceoss)
    webbrowser.open(search)
    time.sleep (1.5)
    exit()

 

PIN_access()
mistake()
initalquestion()

deviceos()
devq1()
