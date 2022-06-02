#Create def to ask user inital question (issue with device or website?)

def initalquestion():
    while True:
        iq=input("""Is your issue regarding a:
        1 - Device
        2 Website
        """)
        if iq == 1:
            print ("You have selected: Device ")
        elif iq == 2:
            print ("You have selected: Website ") 
        else:
            print ("Unrecognised input!")
        contq = input("Do you wish to continue? (y or n").strip().lower()
        if contq == "y":
            print ("Continuing")
            break
        else:
            ()