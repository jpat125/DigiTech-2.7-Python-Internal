#main program v1
#from glob import glob

#pin def
def PIN_access():

    while True:
        userpin=int(input("Enter PIN: "))
        if userpin == 1234:
            print ("access granted")
            print('\n')
            break
        else:
            print ("Please try again:")
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

#Create def to ask user inital question (issue with device or website?)
def initalquestion():
    while True:
        iq=(int(input("""Is your issue regarding a:

1 - Device
2 - Website

""")))
        print ('\n')
        if iq == 1:
            print (devicetype())
        elif iq == 2:
            print (whichweb()) 
        else:
            print ("Unrecognised input!")
        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
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



PIN_access()
initalquestion()
devicetype()
