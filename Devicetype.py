#def asks user for the type of device that is having the issue
from glob import glob


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

devicetype()