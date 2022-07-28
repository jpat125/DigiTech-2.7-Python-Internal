def returntomenu():

    returno=((input("Would you like to re-use this tool?")).strip().lower())

    if returno == "y" or returno == "yes":
        print ("continuing")
        returnq=(input("""Please select an option below:
1 - KAMAR
2 - Google Classroom
3 - Google Drive  
4 - Google docs/slides
5 - Other

""").strip().lower())



    if returnq == "1":
        print ("'Main menu' selected")
    elif returnq == "2":
        print ("'Device Type menu' selected")
    elif returnq == "3":
        print("'Device OS menu' selected")
    elif returnq == "4":
        print ("'Issues menu' selected")
    else:
        print ("Unrecognised input, please try again")

    print ('\n')
    
    if returnq == "1" or returnq =="2" or returnq =="3" or returnq=="4" or returnq=="5":
        contq = input("Have you selected the correct option? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes"):
            if returnq == "1":
                intitalquestion()
            elif returnq == "2":
                devicetype()
            elif returnq == "3":
                deviceos()
            elif returnq == "4":
                devq1
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
    

    elif returno == "n" or returno == "no":
        print ("Exiting...")
        exit()

    else:
        ()
    