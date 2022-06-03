#Create def to ask user inital question (issue with device or website?)

def initalquestion():
    while True:
        iq=input("""Is your issue regarding a:

1 - Device
2 Website

""")
        print ('\n')
        if iq == "1":
            print ("You have selected: Device ")
        elif iq == "2":
            print ("You have selected: Website ") 
        else:
            print ("Unrecognised input!")
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if contq == "y" or contq == "yes":
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            break
        else:
            print("Unrecognised input")
            print ('\n')
        
        
initalquestion()