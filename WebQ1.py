
def whichweb():
     while True:
        whichweb=(int(input("""Please select an option below:
1 - KAMAR
2 - Google Clasroom
3 - Google Drive  
4 - Google docs/slides

""").strip().lower()))
        if whichweb == 1:
            print ("KAMAR selected")
        elif whichweb == 2:
            print ("Google Classroom")
        elif whichweb == 3:
            print("Google Drive")
        elif whichweb == 4:
            print ("Googgle doc/slides")

        print ('\n')
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

whichweb()