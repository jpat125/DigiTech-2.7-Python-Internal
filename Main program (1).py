#main program v1
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
#Create def to ask user inital question (issue with device or website?)
def initalquestion():
    while True:
        iq=(int(input("""Is your issue regarding a:

1 - Device
2 Website

""")))
        print ('\n')
        if iq == 1:
            print ("You have selected: Device ")
        elif iq == 2:
            print ("You have selected: Website ") 
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









PIN_access()
initalquestion()
