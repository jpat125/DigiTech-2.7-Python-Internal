
from shutil import which


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

whichweb()