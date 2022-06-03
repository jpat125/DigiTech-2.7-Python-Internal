#def asks user for the type of device that is having the issue
from glob import glob


def devicetype():
    while True:
        global devty
        devty=int(input("""Please select the type of device you are having an issue with:

    1 - Laptop
    2 - Ipad (Apple only)
    3 - Tablet
    4 - Apple Mac
    """))  

        if devty == "1":
            print ("laptop")
        elif devty == "2":
            print ("Ipad")
        elif devty == "3":
            print ("Tablet")
        elif devty == "4":
            print ("Apple Mac")
        else:
            print ("Unrecognised input")
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
            