# main program v4
import webbrowser
import time
import pyperclip
import os
import emoji

# /*  .oooooo.                             .                           .              .o8                                oooo
# d8P'  `Y8b                          .o8                         .o8             "888                                   `888
# 888           .ooooo.  ooo. .oo.   .o888oo  .oooo.    .ooooo.  .o888oo       .oooo888   .ooooo.  oooo    ooo  .ooooo.   888   .ooooo.  oo.ooooo.   .ooooo.  oooo d8b
# 888          d88' `88b `888P"Y88b    888   `P  )88b  d88' `"Y8   888        d88' `888  d88' `88b  `88.  .8'  d88' `88b  888  d88' `88b  888' `88b d88' `88b `888""8P
# 888          888   888  888   888    888    .oP"888  888         888        888   888  888ooo888   `88..8'   888ooo888  888  888   888  888   888 888ooo888  888
# `88b    ooo  888   888  888   888    888 . d8(  888  888   .o8   888 .      888   888  888    .o    `888'    888    .o  888  888   888  888   888 888    .o  888
# `Y8bood8P'  `Y8bod8P' o888o o888o   "888" `Y888""8o `Y8bod8P'   "888"      `Y8bod88P" `Y8bod8P'     `8'     `Y8bod8P' o888o `Y8bod8P'  888bod8P' `Y8bod8P' d888b
#                                                                                                                                        888
#                                                                                                                                       o888o

mistake = ("If you belive I have made a mistake, please contact my devloper at: jpatel@students.mags.school.nz")


# /*oooooooooooo                                 o8o  o8o
# `888'     `8                                 `"'  `"'
# 888         ooo. .oo.  .oo.    .ooooo.     oooo oooo   .oooo.o
# 888oooo8    `888P"Y88bP"Y88b  d88' `88b    `888 `888  d88(  "8
# 888    "     888   888   888  888   888     888  888  `"Y88b.
# 888       o  888   888   888  888   888     888  888  o.  )88b
# o888ooooood8 o888o o888o o888o `Y8bod8P'     888 o888o 8""888P'
#                                             888
#                                         .o. 88P
#                                         `Y888P

error_emoji = (emoji.emojize(':red_exclamation_mark:'))


#/*  .oooooo.       .   oooo                                                                                        
# d8P'  `Y8b    .o8   `888                                                                                        
#888      888 .o888oo  888 .oo.    .ooooo.  oooo d8b       .ooooo.  oooo d8b oooo d8b  .ooooo.  oooo d8b  .oooo.o 
#888      888   888    888P"Y88b  d88' `88b `888""8P      d88' `88b `888""8P `888""8P d88' `88b `888""8P d88(  "8 
#888      888   888    888   888  888ooo888  888          888ooo888  888      888     888   888  888     `"Y88b.  
#`88b    d88'   888 .  888   888  888    .o  888          888    .o  888      888     888   888  888     o.  )88b 
# `Y8bood8P'    "888" o888o o888o `Y8bod8P' d888b         `Y8bod8P' d888b    d888b    `Y8bod8P' d888b    8""888P' 
                                                                                                                 
def othererror():
    
    oerrorc=input("""What catagory is the isssue related to? 

    1 - Display issue (including projecting)
    2 - Wi-Fi issues
    3 - Printing issues
    4 - Audio issues
    5 - Other

    *Type the number next to option below and press 'ENTER' after typing*

    """)

    oerrordos = input("""What device and Operating System are you using?

    *Type then press 'ENTER' after typing*

    """)

    oerrordesc = input("""Please describe the error in full detail and how you came across it:

    *Type out then press 'ENTER' after typing*

    """)


    oerrorlformat={"Catagory":oerrorc,
    "Device type and OS":oerrordos,
    "Description":oerrordesc
    }

    othererrorslog = [] 

    othererrorslog.append(oerrorlformat)

    print (othererrorslog)

    oels=str(othererrorslog)

    file_object = open('othererrors.txt', 'a')
    file_object.write('\n')
    file_object.write(oels)

    file_object.close()                                                                                                             
                            



# /*ooooooooo.   ooooo ooooo      ooo
# `888   `Y88. `888' `888b.     `8'
#  888   .d88'  888   8 `88b.    8        .oooo.    .ooooo.   .ooooo.   .ooooo.   .oooo.o  .oooo.o
#  888ooo88P'   888   8   `88b.  8       `P  )88b  d88' `"Y8 d88' `"Y8 d88' `88b d88(  "8 d88(  "8
#  888          888   8     `88b.8        .oP"888  888       888       888ooo888 `"Y88b.  `"Y88b.
#  888          888   8       `888       d8(  888  888   .o8 888   .o8 888    .o o.  )88b o.  )88b
# o888o        o888o o8o        `8       `Y888""8o `Y8bod8P' `Y8bod8P' `Y8bod8P' 8""888P' 8""888P'

# PIN function - controls and resticts access to program to only PIN holders (MAGS staff and students)
def PIN_access():

    global studentuserpin
    global staffuserpin
    global userpini
    while True:
        wave = (emoji.emojize(':waving_hand:'))
        print (wave,"Hi there!\nThis is an automated IT support tool for Mount Albert Grammar School staff and students.")

        try:
            # Try to convert the input into a number
            userpini = int(input("Enter your PIN:  "))

        # checki=(userpin.isnumeric())

            studentuserpin = 1234
            staffuserpin = 12345

            if (userpini == studentuserpin):  # and (checki==True):
                print("MAGS Student access granted")
                print('\n')
                break
            elif (userpini == staffuserpin):  # and (checki==True):
                print("MAGS Staff access granted")
                print('\n')
                break
            else:
                print("Incorrect input, please try again:")
                print('\n')

        except ValueError:       # Do this instead if the try block causes a ValueError
            print("Sorry, that is not a valid PIN. Please try again.")
            print('\n')


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

# Create def to ask user initial question (issue with device or website?)
def initialquestion():
    global iq

    while True:
        # device_emoji=(emoji.emojize(':desktop_computer:'))
        # web_emoji=(emoji.emojize(':globe_with_meridians:'))
        iq = (input("""Is your issue regarding a:

1 - BYOD, School or Staff Device
2 - Website

*Type the number next to option below and press 'ENTER' after typing*

"""))

        if iq == "1":
            print(f"You have selected: Issue with a Device")
        elif iq == "2":
            print(f"You have selected: Issue with a Website")
        else:
            print ('\n')
            print(f"{error_emoji}I'm sorry, I don't think that's an option!\n"+mistake)
            print('\n')

        if iq == "1" or iq == "2":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if (contql == "y" or contql == "yes"):
                print("Continuing")
                print('\n')
                if iq == "1":
                    return (devicetype())
                elif iq == "2":
                    return (whichweb())

            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')

            else:
                print(f"{error_emoji}Unrecognised input {error_emoji}")
                print('\n')


# resource db to go here:

# /*ooooooooo.
# `888   `Y88.
#  888   .d88'  .ooooo.   .oooo.o  .ooooo.  oooo  oooo  oooo d8b  .ooooo.   .ooooo.   .oooo.o
#  888ooo88P'  d88' `88b d88(  "8 d88' `88b `888  `888  `888""8P d88' `"Y8 d88' `88b d88(  "8
#  888`88b.    888ooo888 `"Y88b.  888   888  888   888   888     888       888ooo888 `"Y88b.
#  888  `88b.  888    .o o.  )88b 888   888  888   888   888     888   .o8 888    .o o.  )88b
# o888o  o888o `Y8bod8P' 8""888P' `Y8bod8P'  `V88V"V8P' d888b    `Y8bod8P' `Y8bod8P' 8""888P'

website_resources=[
    {"KAMAR": "https://drive.google.com/file/d/16K9lJfnL3C9IF913k29JYJDTiXMdrtNS/view"},
    {"KAMAR students":"https://drive.google.com/file/d/1lM3Pm6HS9T5NMb8cUe2mnFgepn1KIG3d/view"},
    {"mags google classroom": "https://drive.google.com/file/d/1uAGse14fctRMNYP-3t28VuKLi79Y5XAq/view"},
    {"google classroom":"https://support.google.com/edu/classroom/?hl=en-GB&authuser=0#topic=10298088"},
    {"google drive": "https://support.google.com/drive/?hl=en#topic=14940"},
    {"google docs/slides": "https://support.google.com/docs/?hl=en#topic=1382883"}
    ]

displayappletv = [
    {"macOS":"https://drive.google.com/file/d/1_eXdfVO4nRM_LLPizo9hWQtqul91OAbw/view?usp=sharing"}
]
displaymirroring = [
    {"win10/11": "https://drive.google.com/file/d/1Lcqxyu1V3Ux5n3U7_t3FQlk_shnTFlem/view?usp=sharing"},
    {"macOS": "https://drive.google.com/file/d/1cf2DiJSysehx9bMe8kMZXQsfhKdwsHwl/view?usp=sharing"}
]
displaymonitor = [
    {"win10": "https://drive.google.com/file/d/11cTYSBwgbVK_A3CK0hyCAuHVPsX62OoV/view?usp=sharing"},
    {"win11": "https://drive.google.com/file/d/1XJcZodhqdsZootrNOwhm0yENvMtlNec8/view?usp=sharing"},
    {"macOS": "https://drive.google.com/file/d/1rcsKU7H14xK5pZoheyIC0-aI5S3J88Vs/view?usp=sharing"},
    {"iPadOS": "https://drive.google.com/file/d/1oaxtQBz0YE9F19HFYO9fR5RgXdlwhC0l/view"}
]

audioconnect = [
    {"win10": "https://drive.google.com/file/d/1KnkxN617MFcKG_Yo95xtZw4vE7tO0c1h/view?usp=sharing"},
    {"win11": "https://drive.google.com/file/d/1FehHSMAIIBheyqeIJqlIE9c0utXIstOt/view?usp=sharing"},
    {"macOS": "https://drive.google.com/file/d/1FOhVpn30CN4Fj0DJwkFZpoR2HB9Qkij2/view?usp=sharing"}
]

wifi = [
    {"connectingstudents":"C:/Users/JP (School)/OneDrive - Mount Albert Grammar School/Desktop/Digital Tech VS Code/2.7 Internal/MAGS-BYOD-booklet-2022-V2.pdf"}
]
printing = [
    {"printpin": "https://drive.google.com/file/d/1_c7usYyc0CTCGd8SgoJAvnoGQXVf0Djg/view"},
    {"print": "https://drive.google.com/file/d/1_c7usYyc0CTCGd8SgoJAvnoGQXVf0Djg/view"}
]

# /*oooooo   oooooo     oooo oooo         o8o            oooo                                         .o8                 o8o      .
#  `888.    `888.     .8'  `888         `"'            `888                                        "888                 `"'    .o8
#   `888.   .8888.   .8'    888 .oo.   oooo   .ooooo.   888 .oo.        oooo oooo    ooo  .ooooo.   888oooo.   .oooo.o oooo  .o888oo  .ooooo.
#    `888  .8'`888. .8'     888P"Y88b  `888  d88' `"Y8  888P"Y88b        `88. `88.  .8'  d88' `88b  d88' `88b d88(  "8 `888    888   d88' `88b
#     `888.8'  `888.8'      888   888   888  888        888   888         `88..]88..8'   888ooo888  888   888 `"Y88b.   888    888   888ooo888
#      `888'    `888'       888   888   888  888   .o8  888   888          `888'`888'    888    .o  888   888 o.  )88b  888    888 . 888    .o
#       `8'      `8'       o888o o888o o888o `Y8bod8P' o888o o888o          `8'  `8'     `Y8bod8P'  `Y8bod8P' 8""888P' o888o   "888" `Y8bod8P'



# webq1
def whichweb():
    while True:
        whichweb = (input(f"""Please select an option below:
1 - KAMAR
2 - Google Classroom
3 - Google Drive
4 - Google docs/slides
5 - Other

*Type the number next to option below and press 'ENTER' after typing*

""").strip().lower())

        if whichweb == "1":
            print("'KAMAR' selected")
        elif whichweb == "2":
            print("'Google Classroom' selected")
        elif whichweb == "3":
            print("'Google Drive' selected")
        elif whichweb == "4":
            print("'Google doc/slides' selected")
        elif whichweb == "5":
            print("'Other' selected")
        else:
            print("Unrecognised input, please try again")

        print('\n')

        if whichweb == "1" or whichweb == "2" or whichweb == "3" or whichweb == "4" or whichweb == "5":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if (contql == "y" or contql == "yes"):
                if (whichweb == "1") and (userpini == staffuserpin):
                    webbrowser.open(website_resources[0]['KAMAR'])
                    returntomenu()
                elif (whichweb == "1") and (userpini == studentuserpin):
                    webbrowser.open(website_resources[1]['KAMAR students'])
                    returntomenu()
                elif whichweb == "2" and (userpini == staffuserpin):
                    webbrowser.open(website_resources[2]['mags google classroom'])
                    returntomenu()
                elif whichweb == "2" and (userpini == studentuserpin):
                    webbrowser.open(website_resources[3]['google classroom'])
                elif whichweb == "3":
                    webbrowser.open(website_resources[4]['google drive'])
                    returntomenu()
                elif whichweb == "4":
                    webbrowser.open(website_resources[5]["google docs/slides"])
                    returntomenu()
                elif whichweb == "5":
                    googlesearch()
                    returntomenu()
                else:
                    ()
                print("Continuing")
                print('\n')

            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')

            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")
                print('\n')


# /*oooooooooo.                          o8o                          .
# `888'   `Y8b                         `"'                        .o8
#  888      888  .ooooo.  oooo    ooo oooo   .ooooo.   .ooooo.  .o888oo oooo    ooo oo.ooooo.   .ooooo.
#  888      888 d88' `88b  `88.  .8'  `888  d88' `"Y8 d88' `88b   888    `88.  .8'   888' `88b d88' `88b
#  888      888 888ooo888   `88..8'    888  888       888ooo888   888     `88..8'    888   888 888ooo888
#  888     d88' 888    .o    `888'     888  888   .o8 888    .o   888 .    `888'     888   888 888    .o
# o888bood8P'   `Y8bod8P'     `8'     o888o `Y8bod8P' `Y8bod8P'   "888"     .8'      888bod8P' `Y8bod8P'
#                                                                       .o..P'       888                                                                                     `Y8P'       o888o
# def asks user for the type of device that is having the issue

def devicetype():
    global devty
    while True:
        devty = (input("""Please type out the number next to the type of device you are having an issue with:

1 - Laptop
2 - Ipad (Apple only)
3 - Tablet
4 - Apple Mac
5 - Other

*Type the number next to option below and press 'ENTER' after typing*

"""))

        if devty == "1":
            print("You have selected: Laptop")

        elif devty == "2":
            print("You have selected: Ipad")

        elif devty == "3":
            print("You have selected: Tablet")

        elif devty == "4":
            print("You have selected: Apple Mac")

        elif devty == "5":
            print("You have selected: Other")
            print("I'm sorry, I don't have resources to help you, I recommend you contact IT helpdesk")
            helpdesk()


        else:
            print(f"{error_emoji}Unrecognised input{error_emoji}")

        print('\n')

        if devty == "1" or devty == "2" or devty == "3" or devty == "4" or devty == "5":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if (contql == "y" or contql == "yes") and (devty == "1" or devty == "2" or devty == "3" or devty == "4" or devty == "5"):
                print("Continuing")
                print('\n')
                break
                exit()

            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')

            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")
                print('\n')
        else:
            ()

# /*oooooooooo.                          o8o                        .oooooo.    .oooooo..o
# `888'   `Y8b                         `"'                       d8P'  `Y8b  d8P'    `Y8
#  888      888  .ooooo.  oooo    ooo oooo   .ooooo.   .ooooo.  888      888 Y88bo.
#  888      888 d88' `88b  `88.  .8'  `888  d88' `"Y8 d88' `88b 888      888  `"Y8888o.
#  888      888 888ooo888   `88..8'    888  888       888ooo888 888      888      `"Y88b
#  888     d88' 888    .o    `888'     888  888   .o8 888    .o `88b    d88' oo     .d8P
# o888bood8P'   `Y8bod8P'     `8'     o888o `Y8bod8P' `Y8bod8P'  `Y8bood8P'  8""88888P'
# devOS


def deviceos():
    global deviceoss

    while True:
        deviceosv = (input("What is the Operating System of the device? eg. Windows 10, IpadOS, macOS (if unknown, type 'uknown') *Press enter after typing* ").strip().lower().replace(" ", ""))
        deviceoss = ()
        if deviceosv == "windows10" or deviceosv == "win10":
            deviceoss = ("windows10")
            print("'Windows 10' selected")
        elif deviceosv == "windows11" or deviceosv == "win11":
            deviceoss = ("windows11")
            print("'Windows 11' selected ")
        elif deviceosv == "ipados" or deviceosv == "ipad":
            deviceoss = ("ipados")
            print("'IpadOS' selected")
        elif deviceosv == "macos" or deviceosv == "mac":
            deviceoss = ("macos")
            print("'macOS' selected")
        elif deviceosv == "unknown" or deviceosv == "other":
            print("I'm sorry, I don't have resources to help you, I recommend you contact IT helpdesk")
            return helpdesk()
            
            
            
        else:
            print(f"{error_emoji}That doesn't seem to be a supported Operating System, perphaps you have mispelt?{error_emoji}")
            print('\n')
        if deviceoss == "macos" or deviceoss == "windows10" or deviceoss == "windows11" or deviceoss == "ipados":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if contql == "y" or contql == "yes":
                print("Continuing")
                print('\n')
                break
            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')

            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")
                print('\n')
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
# deviceQ1


def devq1():
    global devq1v
    while True:
        devq1v = (input("""Please pick the option that best represent's your issue:
1 - Display issue (including projecting)
2 - Wi-Fi issues
3 - Printing issues
4 - Audio issues
5 - Error code(s)
6 - Other issue (logs issue)
7 - Contact Helpdesk

*Type the number next to option below and press 'ENTER' after typing*

""").strip().lower())

        if devq1v == "1":
            print("Display issue selected")
        elif devq1v == "2":
            print("Wi-Fi issue selected")
        elif devq1v == "3":
            print("Printing issue selected")
        elif devq1v == "4":
            print("Audio issue selected")
        elif devq1v == "5":
            print("Error code search selected")
        elif devq1v == "6":
            print("Other issue selected")
        elif devq1v == "7":
            print("Contact Helpdesk selected")

        if devq1v == "1" or devq1v == "2" or devq1v == "3" or devq1v == "4" or devq1v == "5" or devq1v == "6" or devq1v == "7":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if (contql == "y" or contql == "yes"):
                print("Continuing")
                print('\n')
                if devq1v == "1":
                    return (displayissue())  # leads to display issues question
                elif devq1v == "2":
                    return (wifissue())  # leads to wifi issues question
                elif devq1v == "3":
                    # leads to print issues issues question
                    return (printissue())
                elif devq1v == "4":
                    return (audioissue())  # leads to audio issues question
                elif devq1v == "5":
                    return (errorcodesearch())  # leads to google search
                elif devq1v == "6":
                    return (othererror())  # lead to google search
                elif devq1v == "7":
                    return (helpdesk())  # throws up helpdesk email address
                
                else:
                    print(f"{error_emoji}Unrecognised input{error_emoji}")

                    print('\n')

            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')

            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")
                print('\n')


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
# display issue


def displayissue():
    while True:
        auth = ('')
        displayissue = (input("""Please type the number that best represents your display issue:
    1 - Issue with Apple TV
    2 - Issue with mirroring
    3 - Issue with connecting to monitor/projector
    4 - Other 

*Type the number next to option below and press 'ENTER' after typing*

"""))
        no_access=(emoji.emojize(':no_entry:'))
        if (displayissue == "1") and (userpini == staffuserpin):
            print("Apple TV selected")

        elif displayissue == "2":
            print("mirroring selected")
        elif displayissue == "3":
            print("Monitor selected")
        elif displayissue == "4":
            print("Other selected")
        else:
            print(f"{no_access} Either you don't have access to this or you have input an unrecognised input, please try again {no_access}")
            auth = ("false")
        print('\n')
        if displayissue == "1" or displayissue == "2" or displayissue == "3" or displayissue == "4" and auth == "":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()

            print('\n')
            if contql == "y" or contql == "yes":                
                print("Continuing")
                print('\n')

            elif contql == "n" or contql == "no" :
                print("Stopping")
                print('\n')
            else:
                print(f"{error_emoji}Unrecognised input{error_emoji}")
                print('\n')

                if (displayissue == "1") and (deviceoss == "macos"):
                    webbrowser.open(displayappletv[0]['macOS'])
                    
                elif (displayissue == "2") and (deviceoss == "macos"):
                    webbrowser.open(displaymirroring[1]["macOS"])
                    returntomenu()
                elif (displayissue == "2") and (deviceoss == "windows10"):
                    webbrowser.open(displaymirroring[0]["win10/11"])
                    #returntomenu()
                    return (returntomenu())
                elif (displayissue == "2") and (deviceoss == "windows11"):
                    (webbrowser.open (displaymirroring[2]["win10/11"]))
                    returntomenu()
                elif (displayissue == "3") and (deviceoss == "macos"):
                    webbrowser.open(displaymonitor[2]["macOS"])
                    returntomenu()
                elif (displayissue == "3") and (deviceoss == "windows10"):
                    webbrowser.open(displaymonitor[0]["win10"])
                    returntomenu()
                elif (displayissue == "3") and (deviceoss == "windows11"):
                    webbrowser.open(displaymonitor[1]["win11"])
                    returntomenu()
                elif (displayissue == "3") and (deviceoss ==" ipados"):
                    webbrowser.open(displaymonitor[3]["iPadOS"])
                elif displayissue == "4":
                    googlesearch()
                else:
                    print(
                        f"{error_emoji}Chosen device OS not compatible with this option{error_emoji}")
        else:
            ()

# /*      .o.                         .o8   o8o                 ooooo
#      .888.                       "888   `"'                 `888'
#     .8"888.     oooo  oooo   .oooo888  oooo   .ooooo.        888   .oooo.o  .oooo.o oooo  oooo   .ooooo.
#    .8' `888.    `888  `888  d88' `888  `888  d88' `88b       888  d88(  "8 d88(  "8 `888  `888  d88' `88b
#   .88ooo8888.    888   888  888   888   888  888   888       888  `"Y88b.  `"Y88b.   888   888  888ooo888
#  .8'     `888.   888   888  888   888   888  888   888       888  o.  )88b o.  )88b  888   888  888    .o
# o88o     o8888o  `V88V"V8P' `Y8bod88P" o888o `Y8bod8P'      o888o 8""888P' 8""888P'  `V88V"V8P' `Y8bod8P'

# audio issue


def audioissue():
    while True:

        audioissuev = (input("""I am having issues with:
1 - Connecting to projector or TV
2 - Connecting to speakers
3 - Other

*Type the number next to option below and press 'ENTER' after typing*

"""))
        if audioissuev == "1":
            print("connecting to projector/tv")

        elif audioissuev == "2":
            print("connecting to speakers")

        elif audioissuev == "3":
            print("Other")

        else:
            print("Unrecognised input, please try again")

        print('\n')

        if audioissuev == "1" or audioissuev == "2" or audioissuev == "3":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if (contql == "y" or contql == "yes") and (audioissuev == "1" or audioissuev == "2" or audioissuev == "3"):
                print("Continuing")
                print('\n')

            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')
            else:
                print("Unrecognised input")
                print('\n')

                if (audioissuev == "1") and (deviceoss == "windows10"):
                    webbrowser.open(audioconnect[0]["win10"])
                    returntomenu()
                elif (audioissuev == "1") and (deviceoss == "windows11"):
                    webbrowser.open(audioconnect[1]["win11"])
                    returntomenu()
                elif (audioissuev == "1") and (deviceoss == "macos"):
                    webbrowser.open(audioconnect[2]["macOS"])
                    returntomenu()
                elif (audioissuev == "2") and (deviceoss == "windows10"):
                    webbrowser.open(audioconnect[0]["win10"])
                    returntomenu()
                elif (audioissuev == "2") and (deviceoss == "windows11"):
                    webbrowser.open(audioconnect[1]["win11"])
                    returntomenu()
                elif (audioissuev == "2") and (deviceoss == ["macos"]):
                    webbrowser.open(audioconnect[2]["macOS"])
                    returntomenu()
                elif audioissuev == "3":
                    helpdesk()
                    
        else:
            print("Chosen device OS not compatible with this option")

# /*oooooo   oooooo     oooo  o8o   .o88o.  o8o        o8o
#  `888.    `888.     .8'   `"'   888 `"  `"'        `"'
#   `888.   .8888.   .8'   oooo  o888oo  oooo       oooo   .oooo.o  .oooo.o oooo  oooo   .ooooo.
#    `888  .8'`888. .8'    `888   888    `888       `888  d88(  "8 d88(  "8 `888  `888  d88' `88b
#     `888.8'  `888.8'      888   888     888        888  `"Y88b.  `"Y88b.   888   888  888ooo888
#      `888'    `888'       888   888     888        888  o.  )88b o.  )88b  888   888  888    .o
#       `8'      `8'       o888o o888o   o888o      o888o 8""888P' 8""888P'  `V88V"V8P' `Y8bod8P'


# wifi issue


def wifissue():
    while True:
        wifiissuev = (input("""I am having issues with:
1 - Connecting
2 - Other

*Type the number next to option below and press 'ENTER' after typing*

"""))

        if wifiissuev == "1":
            print("connecting issues")

        elif wifiissuev == "2":
            print("Other")

        else:
            print("Unrecognised input, please try again")

        print('\n')

        if wifiissuev == "1" or wifiissuev == "2":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if (contql == "y" or contql == "yes") and (wifiissuev == "1" or wifiissuev == "2" or wifiissuev == "3"):
                print("Continuing")
                print('\n')

            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')
            else:
                print("Unrecognised input")
                print('\n')

                if (wifiissuev == "1") and (deviceoss == "windows10") or (deviceoss == "windows11") or (deviceoss == "ipados"):
                    
                    path=("C:/Users/JP (School)/OneDrive - Mount Albert Grammar School/Desktop/Digital Tech VS Code/2.7_Internal/MAGS BYOD booklet.pdf")
                    webbrowser.open_new(path)
                    returntomenu()
                
                elif (wifiissuev == "2"):
                    helpdesk()

        else:
            print(
                "Either you don't have access to this or you have input an unrecognised input, please try again")


# /*ooooooooo.             o8o                  .         o8o
# `888   `Y88.           `"'                .o8         `"'
#  888   .d88' oooo d8b oooo  ooo. .oo.   .o888oo      oooo   .oooo.o  .oooo.o oooo  oooo   .ooooo.
#  888ooo88P'  `888""8P `888  `888P"Y88b    888        `888  d88(  "8 d88(  "8 `888  `888  d88' `88b
#  888          888      888   888   888    888         888  `"Y88b.  `"Y88b.   888   888  888ooo888
#  888          888      888   888   888    888 .       888  o.  )88b o.  )88b  888   888  888    .o
# o888o        d888b    o888o o888o o888o   "888"      o888o 8""888P' 8""888P'  `V88V"V8P' `Y8bod8P'
# print issue


def printissue():
    while True:

        printissuev = (input("""I am having issues with:
1 - Setting printing PIN
2 - Printing in Black & White/Colour
3 - Other

*Type the number next to option below and press 'ENTER' after typing*

"""))

        if printissuev == "1":
            print("'Printing PIN issue' selected")

        elif printissuev == "2":
            print("'Printing issue' selected")

        elif printissuev == "3":
            print("'Other' selected")

        else:
            print("Unrecognised input, please try again")

        print('\n')

        if printissuev == "1" or printissuev == "2" or printissuev == "3":
            contq = input("Have you selected the correct option? (y or n) ")
            contql = contq.strip().lower()
            print('\n')
            if (contql == "y" or contql == "yes") and (printissuev == "1" or printissuev == "2" or printissuev == "3"):
                print("Continuing")
                print('\n')

            elif contql == "n" or contql == "no":
                print("Stopping")
                print('\n')
            else:
                print("Unrecognised input")
                print('\n')

                if printissuev == "1":
                    webbrowser.open(printing[0]["printpin"])
                    returntomenu()
                elif printissuev == "2":
                    webbrowser.open(printing[1]["print"])
                    returntomenu()
                elif printissuev == "3":
                    helpdesk()
                    returntomenu()
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
# google search


def googlesearch():
    taburl = ("https://www.google.com/search?q=")
    querey = (input("Input query: "))
    search = (taburl+querey)
    webbrowser.open(search)
    time.sleep(1.5)
    returntomenu()

# /*oooooooooooo                                                                .o8                                                                 oooo
# `888'     `8                                                               "888                                                                 `888
#  888         oooo d8b oooo d8b  .ooooo.  oooo d8b  .ooooo.   .ooooo.   .oooo888   .ooooo.        .oooo.o  .ooooo.   .oooo.   oooo d8b  .ooooo.   888 .oo.
#  888oooo8    `888""8P `888""8P d88' `88b `888""8P d88' `"Y8 d88' `88b d88' `888  d88' `88b      d88(  "8 d88' `88b `P  )88b  `888""8P d88' `"Y8  888P"Y88b
#  888    "     888      888     888   888  888     888       888   888 888   888  888ooo888      `"Y88b.  888ooo888  .oP"888   888     888        888   888
#  888       o  888      888     888   888  888     888   .o8 888   888 888   888  888    .o      o.  )88b 888    .o d8(  888   888     888   .o8  888   888
# o888ooooood8 d888b    d888b    `Y8bod8P' d888b    `Y8bod8P' `Y8bod8P' `Y8bod88P" `Y8bod8P'      8""888P' `Y8bod8P' `Y888""8o d888b    `Y8bod8P' o888o o888o

# error code


def errorcodesearch():
    taburl = ("https://www.google.com/search?q=")
    errorcode = (input("Input error code: "))
    search = (taburl+"Error code "+errorcode+" "+deviceoss)
    webbrowser.open(search)
    time.sleep(1.5)
    returntomenu()


# /*ooooooooo.                 .                                             .
# `888   `Y88.             .o8                                           .o8
# 888   .d88'  .ooooo.  .o888oo oooo  oooo  oooo d8b ooo. .oo.        .o888oo  .ooooo.       ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo  oooo
# 888ooo88P'  d88' `88b   888   `888  `888  `888""8P `888P"Y88b         888   d88' `88b      `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  `888
# 888`88b.    888ooo888   888    888   888   888      888   888         888   888   888       888   888   888  888ooo888  888   888   888   888
# 888  `88b.  888    .o   888 .  888   888   888      888   888         888 . 888   888       888   888   888  888    .o  888   888   888   888
# o888o  o888o `Y8bod8P'   "888"  `V88V"V8P' d888b    o888o o888o        "888" `Y8bod8P'      o888o o888o o888o `Y8bod8P' o888o o888o  `V88V"V8P'





def returntomenu():
    while True:
        global returnq
        returno = (input("Would you like to re-use this tool? "))
        returnol = returno.strip().lower()
        if returnol == "y" or returnol == "yes":
            print("continuing")
            print ('\n')
            returnq = (input("""Please select an option below:
1 - Login menu
2 - Main menu
3 - Device Type menu
4 - Device OS menu
5 - Issues menu
6 - Exit this program (Choosing this option will close this program)

*Type the number next to option below and press 'ENTER' after typing*

"""))
            returnql=returnq.strip().lower()
           
            if returnql == "1":
                print ("'Login' selected")
            elif returnql == "2":
                print("'Main menu' selected")
            elif returnql == "3":
                print("'Device Type menu' selected")
            elif returnql == "4":
                print("'Device OS menu' selected")
            elif returnql == "5":
                print("'Issues menu' selected")
            elif returnql == "6":
                print("'Exit program' selected")
            else:
                print("Unrecognised input, please try again")

            print('\n')

            if returnql == "1" or returnql == "2" or returnql == "3" or returnql == "4" or returnql == "5" or returnql == "6":
                contq = input("Have you selected the correct option? (y or n) ")
                contql = contq.strip().lower()
                print('\n')
                if (contql == "y" or contql == "yes"):
                    if returnql == "1":
                        return PIN_access() 
                    elif returnql == "2":
                        return initialquestion()
                    elif returnql == "3":
                        return devicetype()
                    elif returnql == "4":
                        return deviceos()
                    elif returnql == "5":
                        return devq1()
                    elif returnql == "6":
                        print("Exiting...")
                        time.sleep(3)
                        exit()
                    else:
                        ()

                elif contql == "n" or contql == "no":
                    print("Stopping")
                    print('\n')

                else:
                    print(f"Unrecognised input")
                    print('\n')

        elif returnol == "n" or returnol == "no":
            print("Exiting...")
            time.sleep(3)
            exit()

        else:
            print(f"Unrecognised input, please try again")
            print ('\n')



# /*ooooo   ooooo           oooo                   .o8                     oooo                                                    o8o  oooo
# `888'   `888'           `888                  "888                     `888                                                    `"'  `888
#  888     888   .ooooo.   888  oo.ooooo.   .oooo888   .ooooo.   .oooo.o  888  oooo        .ooooo.  ooo. .oo.  .oo.    .oooo.   oooo   888
#  888ooooo888  d88' `88b  888   888' `88b d88' `888  d88' `88b d88(  "8  888 .8P'        d88' `88b `888P"Y88bP"Y88b  `P  )88b  `888   888
#  888     888  888ooo888  888   888   888 888   888  888ooo888 `"Y88b.   888888.         888ooo888  888   888   888   .oP"888   888   888
#  888     888  888    .o  888   888   888 888   888  888    .o o.  )88b  888 `88b.       888    .o  888   888   888  d8(  888   888   888
# o888o   o888o `Y8bod8P' o888o  888bod8P' `Y8bod88P" `Y8bod8P' 8""888P' o888o o888o      `Y8bod8P' o888o o888o o888o `Y888""8o o888o o888o
#                                888
#                               o888o

# helpdesk email
def helpdesk():
    helpdesk_emoji = (emoji.emojize(':technologist:'))
    print(helpdesk_emoji)
    email = ("helpdesk@mags.school.nz")
    pyperclip.copy(email)
    print(email)
    print("*email address copied to clipboard*")
    print('\n')
    return returntomenu()


 

PIN_access()
initialquestion()

deviceos()
devq1()
